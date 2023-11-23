import cv2
import numpy as np

# Load the image
image = cv2.imread("D:/samplecv.jpg", 0)

# Create a kernel
kernel = np.ones((5,5),np.uint8)

# Perform the closing operation
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Save the result
cv2.imwrite('closed_image.jpg', closing)
