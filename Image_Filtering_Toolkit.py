import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

def apply_grayscale(image_path, output_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, gray)

def apply_sepia(image_path, output_path):
    img = Image.open(image_path)
    width, height = img.size

    depth = 30
    img = img.convert("L")  # Convert to grayscale
    img = img.filter(ImageFilter.GaussianBlur(radius=2))  # Apply blur filter

    img = img.convert("RGB")  # Convert back to RGB

    img = np.array(img)  # Convert PIL image to numpy array
    img[:, :, 0] = img[:, :, 0] + depth * 2
    img[:, :, 1] = img[:, :, 1] + depth
    img[:, :, 2][img[:, :, 2] > 255 - depth] = 255 - depth

    img = Image.fromarray(np.uint8(img))
    img.save(output_path)

def apply_blur(image_path, output_path):
    img = cv2.imread(image_path)
    blurred = cv2.GaussianBlur(img, (21, 21), 0)
    cv2.imwrite(output_path, blurred)

def apply_edge_detection(image_path, output_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite(output_path, edges)

def apply_contrast(image_path, output_path, factor=1.5):
    img = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(img)
    enhanced_img = enhancer.enhance(factor)
    enhanced_img.save(output_path)

def apply_brightness(image_path, output_path, factor=1.5):
    img = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(img)
    enhanced_img = enhancer.enhance(factor)
    enhanced_img.save(output_path)

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
