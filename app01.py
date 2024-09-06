import os

import cv2
import numpy as np
import torch
from flask import Flask, render_template, request, send_file
from segment_anything import SamPredictor, sam_model_registry
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configurations
app.config['UPLOAD_FOLDER'] = r'C:\Users\anany\Desktop\house-ass\uploads'
app.config['PROCESSED_FOLDER'] = r'C:\Users\anany\Desktop\house-ass\processed'
app.config['SAM_CHECKPOINT'] = r'C:\Users\anany\Desktop\house-ass\sam_vit_b_01ec64.pth'

# Initialize SAM model
def initialize_sam_model(checkpoint_path):
    sam_model = sam_model_registry["vit_b"](checkpoint=checkpoint_path)
    sam_model.eval()
    return SamPredictor(sam_model)

@app.route('/')
def index():
    return render_template('index01.html')

@app.route('/', methods=['POST'])
def upload_images():
    if 'room_image' not in request.files or 'wallpaper_image' not in request.files:
        return "No file uploaded", 400

    room_image_file = request.files['room_image']
    wallpaper_image_file = request.files['wallpaper_image']

    # Save the uploaded files
    room_image_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(room_image_file.filename))
    wallpaper_image_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(wallpaper_image_file.filename))

    room_image_file.save(room_image_path)
    wallpaper_image_file.save(wallpaper_image_path)

    room_img = cv2.imread(room_image_path)
    wallpaper_img = cv2.imread(wallpaper_image_path)

    if room_img is None or wallpaper_img is None:
        return "Error: Could not load one or more images.", 400

    # Initialize SAM model
    predictor = initialize_sam_model(app.config['SAM_CHECKPOINT'])
    
    # Set image for segmentation
    predictor.set_image(room_img)
    
    # Example point (adjust as needed) - you might need to adjust this or use different techniques to identify the wall region
    point_coords = np.array([[100, 100]])
    point_labels = np.array([1])

    # Predict the mask
    masks, scores, logits = predictor.predict(
        point_coords=point_coords,
        point_labels=point_labels,
        multimask_output=False
    )

    # Process the mask
    if masks is not None and len(masks) > 0:
        mask = masks[0]

        # Resize the wallpaper to match the dimensions of the mask
        wallpaper_resized = cv2.resize(wallpaper_img, (mask.shape[1], mask.shape[0]))

        # Replace the segmented region with the wallpaper
        room_img[mask > 0] = wallpaper_resized[mask > 0]

        # Ensure the processed folder exists
        if not os.path.exists(app.config['PROCESSED_FOLDER']):
            os.makedirs(app.config['PROCESSED_FOLDER'])

        # Save the processed image
        output_filename = 'room_with_wallpaper.jpg'
        output_filepath = os.path.join(app.config['PROCESSED_FOLDER'], output_filename)
        cv2.imwrite(output_filepath, room_img)

        # Return the processed image
        return send_file(output_filepath, mimetype='image/jpeg')

    return "No valid mask generated.", 400

if __name__ == "__main__":
    app.run(debug=True)
