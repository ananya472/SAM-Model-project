# SAM-Model-project

#Project Description
This web application allows users to upload an image, which is then processed using a segmentation model. The application applies specific updates to the uploaded image, such as changing colors and returns the processed image as the result. Users can see only the updated image after uploading the original.

#Features
Image Upload: Users can upload an image file through a simple web interface.
Image Processing: The uploaded image is processed using a segmentation model to generate an updated version.
Display Processed Image: The application displays only the processed image after the upload is complete.

1. app.py
Main Python script for the Flask application. Manages file uploads, processes images using the segmentation model, and serves the processed image to the user.
2. index.html
HTML file that creates the web page interface for uploading images and displaying results.
3. main.py
Contains the image processing logic, including interactions with the segmentation model and saving the processed images.
4. output_image.jpg
Example output image showing the result of the image processing.
5. room5.jpg
Example input image used for testing the application.







