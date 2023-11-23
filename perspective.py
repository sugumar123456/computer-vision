import cv2
import numpy as np

image_path = "samplecv.jpg"
original_image = cv2.imread(image_path)

if original_image is None:
    print("Error: Could not read the image.")
else:
    src_points = np.float32([[50, 50], [200, 50], [20, 200], [220, 200]])
    dst_points = np.float32([[0, 0], [300, 0], [0, 400], [300, 400]])

    perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)

    transformed_image = cv2.warpPerspective(original_image, perspective_matrix, (300, 400))

    cv2.imshow("Original Image", original_image)
    cv2.imshow("Transformed Image", transformed_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
