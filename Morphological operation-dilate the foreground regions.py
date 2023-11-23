import cv2
import numpy as np

# Load the image
image = cv2.imread('samplecv.jpg', 0)

# Create a kernel
kernel = np.ones((5,5),np.uint8)

# Perform the gradient operation
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

# Save the result
cv2.imwrite('gradient_image.jpg', gradient)
