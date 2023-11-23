import cv2
import numpy as np

def select_roi(image, x, y, width, height):
    roi = image[y:y+height, x:x+width].copy()
    return roi

def paste_roi(source_image, roi, x, y):
    source_image[y:y+roi.shape[0], x:x+roi.shape[1]] = roi

    return source_image

source_image_path = "samplecv.jpg"
source_image = cv2.imread(source_image_path)

if source_image is None:
    print("Error: Could not read the source image.")
else:
    x, y, width, height = 100, 50, 200, 150

    roi = select_roi(source_image, x, y, width, height)

    cv2.imshow("Original Image", source_image)
    cv2.imshow("Selected ROI", roi)

    source_image_copy = source_image.copy()
    result_image = paste_roi(source_image_copy, roi, x, y)

    cv2.imshow("Result Image", result_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
