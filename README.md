# SAM-Model-project

#Project Description(app.py)
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


#Updated Project Description(app01.py)
This web application enables users to upload a room image and a wallpaper image, then processes the room image using a segmentation model to apply the wallpaper to a specific region. The application provides the resulting image with the wallpaper applied to the segmented area.

#Features
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

#Updated Project Description(app02.py)
This web application enables users to upload a room image and a flooring image, then processes the room image using a segmentation model to apply the flororing to a specific region. The application provides the resulting image with the flooring applied to the segmented area.

#Features
Image Upload: Users can upload two images through a simple web interface:
Room Image: The image of the room where the wallpaper will be applied.
flooring Image: The image of the flooring to be applied.
Image Processing: The application processes the uploaded room image using a segmentation model (SAM) to detect a specific region. The detected region is then updated with the flooring image.
Display Processed Image: After processing, the application displays the resulting image with the flooring applied to the identified region. 


1. app02.py
Main Python script for the Flask application. Manages file uploads, processes images using the segmentation model, and serves the processed image to the user.
2. index01.html
HTML file that creates the web page interface for uploading images and displaying results.
4. floor.jpg
Example input image used for testing the application.
6. flooring.jpg
Example flooring use for the testing.



Updated Project Description(app03.py)
This web application allows users to upload a room image and a replacement image (either wallpaper or flooring). The application then processes the room image using a segmentation model to apply the replacement image to a specific region, such as walls or floors. Users receive the modified room image with the replacement image applied to the chosen area.

#Features
Image Upload:

Room Image: Upload an image of the room where the replacement will be applied.
Replacement Image: Upload the image of the wallpaper or flooring to be applied.
Image Processing:

Segmentation: The application uses a segmentation model (SAM) to detect and segment the specified area in the room image.
Replacement Application: The detected region is updated with the uploaded replacement image, which is resized to fit the segmented area.
Display Processed Image:

Result: After processing, the application displays the resulting image with the replacement image applied to the identified region.







