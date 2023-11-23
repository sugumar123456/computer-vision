import cv2
import numpy as np
path="D:\=shubas.png"
img=cv2.imread(path)
if img is None:
    print("Error")
else:
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgblur=cv2.GaussianBlur(imggray,(7,7),0)
    imgoutline=cv2.Canny(imgblur,100,200)
    cv2.imshow("ImageCanny",imgoutline)
    cv2.waitKey(0)
    


