#perform basic Image Handling and processing operations on the image.• Read an image in python 
#and Convert an Image to Blur using GaussianBlur.
#AIM: 
# To Perform Basic Operations to Read Image and Convert to Blur using GaussianBlur.
#PROGRAM

import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path = "samplecv.jpeg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Img Blur",imgBlur)
cv2.waitKey(0)
