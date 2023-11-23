import cv2
import numpy as np

image_path = "samplecv.jpg"
original_image = cv2.imread(image_path)

if original_image is None:
    print("Error: Could not read the image.")
else:
    angle = 45
    scale = 1.5
    rows, cols = original_image.shape[:2]
    center = (cols // 2, rows // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

    transformed_image = cv2.warpAffine(original_image, rotation_matrix, (cols, rows))

    # Display the original and transformed images
    cv2.imshow("Original Image", original_image)
    cv2.imshow("Transformed Image", transformed_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
