import cv2
import numpy as np

def add_watermark(original_image, watermark_image, position=(0, 0), alpha=0.7):
    
    h, w = original_image.shape[:2]
    watermark_resized = cv2.resize(watermark_image, (w, h))

    watermarked_image = original_image.copy()

    cv2.addWeighted(watermark_resized, alpha, watermarked_image, 1 - alpha, 0, watermarked_image)

    return watermarked_image

original_image_path = "samplecv.jpg"
original_image = cv2.imread(original_image_path)

watermark_path = "logo.png"
watermark_image = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)

if original_image is None or watermark_image is None:
    print("Error: Could not read one or both of the images.")
else:
    watermarked_image = add_watermark(original_image, watermark_image, position=(50, 50), alpha=0.5)

    cv2.imshow("Original Image", original_image)
    cv2.imshow("Watermarked Image", watermarked_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
