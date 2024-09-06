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


Updated Project Description
This web application enables users to upload a room image and a wallpaper image, then processes the room image using a segmentation model to apply the wallpaper to a specific region. The application provides the resulting image with the wallpaper applied to the segmented area.

Features
Image Upload: Users can upload two images through a simple web interface:

Room Image: The image of the room where the wallpaper will be applied.
Wallpaper Image: The image of the wallpaper to be applied.
Image Processing: The application processes the uploaded room image using a segmentation model (SAM) to detect a specific region. The detected region is then updated with the wallpaper image.

Display Processed Image: After processing, the application displays the resulting image with the wallpaper applied to the identified region. 


1. app01.py
Main Python script for the Flask application. Manages file uploads, processes images using the segmentation model, and serves the processed image to the user.
2. index01.html
HTML file that creates the web page interface for uploading images and displaying results.
3. main01.py
Contains the image processing logic, including interactions with the segmentation model and saving the processed images.
4. room_with_wallpaper.jpg
Example output image showing the result of the image processing.
5. room6.jpg
Example input image used for testing the application.
6. wallpaper.jpg
Example wallper use for the testing.







