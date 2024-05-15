
# Image Text Overlay Web App

This application is a Flask-based web service that allows users to upload an image and input text. The application then overlays the text repeatedly across the image with color attributes matching the underlying pixel values of the image. The final processed image is displayed on the web page.

## Features

- Upload an image file through a web form.
- Input text to be overlaid onto the image.
- Adjusts image brightness and overlays the text with original image coloring.
- Display processed image in the browser.

## Installation

### Prerequisites

- Python 3.x
- Flask
- PIL

### Setup

To set up and run the application locally, follow the steps below:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the repo directory:
   ```bash
   cd <repo-directory>
   ```
3. Install the necessary Python packages:
   ```bash
   pip install Flask Pillow
   ```
4. Run the application:
   ```bash
   python app.py
   ```

### Local Development Server

By default, Flask will run the application on `http://127.0.0.1:5000/`. Open this URL in your web browser to interact with the application.

## Usage

1. Navigate to `http://127.0.0.1:5000/` in your web browser.
2. Use the form to select an image file from your computer and input the text you want overlaid on the image.
3. Click on 'Upload and Create Image'.
4. The processed image will be displayed below the form.

## Files

- `app.py`: The main Flask application file containing routes and logic for handling image uploads and text overlay.
- `imgText.py`: A Python class for processing images. This script handles opening, manipulating, and saving images.
- `templates/index.html`: HTML file for the web form interface.
- `uploads/`: Default directory where uploaded images can be temporarily stored (if modifications are made to save uploads).

## Note

The images are processed in-memory and, by default, the results are not saved on the server. If you wish to save the processed images, modifications to the `imgText.py` script are necessary.

## Contributing

Feel free to fork this project, open issues, and submit pull requests for improving the application or documentation. Make sure your changes are well-documented.

```