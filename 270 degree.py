import cv2

# Read the image
image_path = "samplecv.jpg"
original_image = cv2.imread(image_path)
window_name='90 degree'
if original_image is None:
    print("Error: Could not read the image.")
else:
    # Perform a 90-degree rotation clockwise along the y-axis
    rotated_image = cv2.rotate(original_image,cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Display the original and rotated images
    cv2.imshow("Original Image", original_image)
    cv2.imshow("Rotated Image", rotated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
