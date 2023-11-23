import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
image_path = "D:\=shubas.png"
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  
# Check if the image is successfully loaded
if img is None:
    print("Error: Image not loaded.")
    exit()

# Perform dilation on the image
kernel = np.ones((5, 5), np.uint8)  
dilated_img = cv2.dilate(img, kernel, iterations=1)

# Display the original and dilated images using matplotlib
plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(dilated_img, cmap='gray'), plt.title('Dilated Image')
plt.show()
