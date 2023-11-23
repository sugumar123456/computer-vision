import cv2
import numpy as np

def detect_corners(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Harris Corner Detection
    corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

    # Threshold the corners
    corners_threshold = 0.01 * corners.max()
    corner_image = image.copy()
    corner_image[corners > corners_threshold] = [0, 0, 255]  # Red color for detected corners

    return corner_image

# Read the image
image_path = "D:/samplecv.jpg"
original_image = cv2.imread(image_path)

if original_image is None:
    print("Error: Could not read the image.")
else:
    # Perform corner detection
    corner_detected_image = detect_corners(original_image)
    cv2.imshow("Corner Detected Image", corner_detected_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
