import cv2
import numpy as np

image_path = "samplecv.jpg"
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if original_image is None:
    print("Error: Could not read the image.")
else:
    kernel_size = 5
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    dilated_image = cv2.dilate(original_image, kernel, iterations=1)

    cv2.imshow("Original Image", original_image)
    cv2.imshow("Dilated Image", dilated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
