# Image_Filtering_Toolkit

This repository contains a set of image filtering functions implemented using OpenCV and PIL. The toolkit includes functions for applying various filters such as grayscale, sepia, blur, edge detection, contrast enhancement, and brightness enhancement.


Features:

1. Grayscale Filter: Converts an image to grayscale.
2. Sepia Filter: Applies a sepia tone effect to an image.
3. Blur Filter: Applies a Gaussian blur to an image.
4. Edge Detection: Detects edges in an image using the Canny edge detection algorithm.
5. Contrast Enhancement: Enhances the contrast of an image.
6. Brightness Enhancement: Enhances the brightness of an image.


Requirements:

OpenCV
PIL (Pillow)
NumPy


Installation:

1. Clone the repository:

    git clone https://github.com/yourusername/Image_Filtering_Toolkit.git

2. Navigate to the project directory:

    cd Image_Filtering_Toolkit

3. Install the required packages:

    pip install opencv-python pillow numpy


Usage:

Place the input image in the project directory and rename it to input.jpg or update the input_image variable in the script.
Run the script:

    python image_filtering.py


Image Filtering Functions:

1. apply_grayscale(image_path, output_path)

  Converts the image at image_path to grayscale and saves it to output_path.

2. apply_sepia(image_path, output_path)

  Applies a sepia tone effect to the image at image_path and saves it to output_path.

3. apply_blur(image_path, output_path)

  Applies a Gaussian blur to the image at image_path and saves it to output_path.

4. apply_edge_detection(image_path, output_path)

  Detects edges in the grayscale image at image_path and saves the result to output_path.

5. apply_contrast(image_path, output_path, factor=1.5)

  Enhances the contrast of the image at image_path by the given factor and saves it to output_path.

6. apply_brightness(image_path, output_path, factor=1.5)

  Enhances the brightness of the image at image_path by the given factor and saves it to output_path.


Example:

    if __name__ == "__main__":
        input_image = 'input.jpg'

        output_grayscale = 'output_grayscale.jpg'
        apply_grayscale(input_image, output_grayscale)
        print(f"Grayscale filter applied. Output saved as {output_grayscale}")

        output_sepia = 'output_sepia.jpg'
        apply_sepia(input_image, output_sepia)
        print(f"Sepia filter applied. Output saved as {output_sepia}")

        output_blur = 'output_blur.jpg'
        apply_blur(input_image, output_blur)
        print(f"Blur filter applied. Output saved as {output_blur}")

        output_edges = 'output_edges.jpg'
        apply_edge_detection(input_image, output_edges)
        print(f"Edge detection filter applied. Output saved as {output_edges}")

        output_contrast = 'output_contrast.jpg'
        apply_contrast(input_image, output_contrast)
        print(f"Contrast enhancement applied. Output saved as {output_contrast}")

        output_brightness = 'output_brightness.jpg'
        apply_brightness(input_image, output_brightness)
        print(f"Brightness enhancement applied. Output saved as {output_brightness}")

Author:

Waqar Ali

Uploaded Date:

July 26, 2024
