import os

import cv2
import numpy as np
from flask import Flask, render_template, request, send_file
from segment_anything import SamPredictor, sam_model_registry
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r'C:\Users\anany\Desktop\house-ass\uploads'
app.config['PROCESSED_FOLDER'] = r'C:\Users\anany\Desktop\house-ass\processed'

# Paths to the model checkpoint
sam_checkpoint = r"C:\Users\anany\Desktop\house-ass\sam_vit_b_01ec64.pth"

# Initialize SAM model and predictor
sam = sam_model_registry["vit_b"](checkpoint=sam_checkpoint)
predictor = SamPredictor(sam)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    image = cv2.imread(filepath)
    if image is None:
        return "Error: Could not load the image", 400

    predictor.set_image(image)

    # Define points (this is how interactive segmentation typically works)
    point_coords = np.array([[100, 100]])  # Example point, adjust based on your image
    point_labels = np.array([1])  # Label for the point (1 for foreground, 0 for background)

    # Generate masks using point-based interaction
    masks, scores, logits = predictor.predict(
        point_coords=point_coords,
        point_labels=point_labels,
        multimask_output=False
    )

    if masks is not None and len(masks) > 0:
        mask = masks[0]
        color = (83, 105, 101)  # Green color for the wall
        image[mask > 0] = color

        os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

        output_filename = 'processed_' + filename
        output_filepath = os.path.join(app.config['PROCESSED_FOLDER'], output_filename)

        cv2.imwrite(output_filepath, image)

        if os.path.exists(output_filepath):
            return send_file(output_filepath, mimetype='image/jpeg')
        else:
            return "Error: Processed file not saved", 500

    return "No valid mask generated", 400

if __name__ == '__main__':
    app.run(debug=True)

