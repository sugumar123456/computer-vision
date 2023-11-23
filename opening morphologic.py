import cv2
import numpy as np

# Read the image
image_path = "D:\=shubas.png"
original_image = cv2.imread(image_path)

if original_image is None:
    print("Error: Could not read the image.")
else:
    # Define the kernel for opening
    kernel_size = 5
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # Perform opening (erosion followed by dilation)
    opened_image = cv2.morphologyEx(original_image, cv2.MORPH_OPEN, kernel)

    # Display the original and opened images
    cv2.imshow("Original Image", original_image)
    cv2.imshow("Opened Image", opened_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
