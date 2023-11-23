import cv2
import numpy as np

# Load the image
image = cv2.imread("D:\=shubas.png", 0)

# Create a kernel
kernel = np.ones((5,5),np.uint8)

# Perform the top hat operation
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

# Save the result
cv2.imwrite("D:\=shubas.png", tophat)
