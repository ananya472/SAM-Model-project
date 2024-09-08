import logging
import os

import cv2
import numpy as np
from flask import Flask, render_template, request, send_file
from segment_anything import SamPredictor, sam_model_registry
from werkzeug.utils import secure_filename

# Flask app initialization
app = Flask(__name__)

# Configurations
app.config['UPLOAD_FOLDER'] = r'C:\Users\anany\Desktop\house-ass\uploads'
app.config['PROCESSED_FOLDER'] = r'C:\Users\anany\Desktop\house-ass\processed'
app.config['SAM_CHECKPOINT'] = r'C:\Users\anany\Desktop\house-ass\sam_vit_b_01ec64.pth'

# Ensure folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

# Enable logging for debugging
logging.basicConfig(level=logging.INFO)

# Initialize SAM model
def initialize_sam_model(checkpoint_path):
    logging.info("Initializing SAM model...")
    sam_model = sam_model_registry["vit_b"](checkpoint=checkpoint_path)
    sam_model.eval()  # Set the model to evaluation mode
    return SamPredictor(sam_model)

# Route for the main page
@app.route('/')
def index():
    return render_template('index02.html')

# Route for processing the images
@app.route('/upload', methods=['POST'])
def upload_images():
    # Check if both images were uploaded
    if 'room_image' not in request.files or 'flooring_image' not in request.files:
        return "Please upload both the room and flooring images.", 400

    # Get the uploaded files
    room_image_file = request.files['room_image']
    flooring_image_file = request.files['flooring_image']

    # Save the uploaded files
    room_image_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(room_image_file.filename))
    flooring_image_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(flooring_image_file.filename))
    room_image_file.save(room_image_path)
    flooring_image_file.save(flooring_image_path)

    # Read the images using OpenCV
    room_img = cv2.imread(room_image_path)
    flooring_img = cv2.imread(flooring_image_path)

    # Check if images were loaded correctly
    if room_img is None or flooring_img is None:
        return "Error loading one or both images.", 400

    # Initialize the SAM model
    predictor = initialize_sam_model(app.config['SAM_CHECKPOINT'])

    # Set the room image in the SAM model
    predictor.set_image(room_img)

    # Coordinates for floor segmentation (manually defined or obtained via a UI)
    floor_point_coords = np.array([[450, 650]])  # Adjust as needed to target the floor area
    floor_point_labels = np.array([1])  # Label indicating it's a foreground point

    # Predict the mask for the floor
    masks, _, _ = predictor.predict(point_coords=floor_point_coords, point_labels=floor_point_labels, multimask_output=False)

    # Process the mask and replace the floor with the uploaded flooring
    if masks is not None and len(masks) > 0:
        floor_mask = masks[0]  # Use the first mask

        # Resize the flooring image to match the dimensions of the mask
        flooring_resized = cv2.resize(flooring_img, (floor_mask.shape[1], floor_mask.shape[0]))

        # Apply the new flooring to the room image using the mask
        room_img[floor_mask > 0] = flooring_resized[floor_mask > 0]

        # Save the processed image
        output_filename = 'room_with_new_flooring.jpg'
        output_filepath = os.path.join(app.config['PROCESSED_FOLDER'], output_filename)
        cv2.imwrite(output_filepath, room_img)

        # Return the processed image
        return send_file(output_filepath, mimetype='image/jpeg')

    return "Failed to generate a mask for the floor.", 400

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
