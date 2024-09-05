import os


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file uploaded", 400
    file = request.files['file']

    # Secure the file and save it to the uploads folder
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Load the uploaded image using OpenCV
    image = cv2.imread(filepath)

    if image is None:
        return "Error: Could not load the image", 400

    # Set image for segmentation
    predictor.set_image(image)

    # Example point (adjust as needed)
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
        color = (83, 105, 101)
        image[mask > 0] = color

        # Ensure the processed folder exists
        processed_folder = app.config['PROCESSED_FOLDER']
        os.makedirs(processed_folder, exist_ok=True)

        # Save the processed image
        output_filename = 'processed_' + filename
        output_filepath = os.path.join(processed_folder, output_filename)

        # Debugging - Check folder path and file
        print(f"Processed folder exists: {os.path.exists(processed_folder)}")
        print(f"Saving file to: {output_filepath}")

        # Save the image
        cv2.imwrite(output_filepath, image)

        # Check if the file was saved
        if os.path.exists(output_filepath):
            print(f"File saved successfully: {output_filepath}")
            return send_file(output_filepath, mimetype='image/jpeg')
        else:
            return "Error: Processed file not saved", 500

    return "No valid mask generated", 400
