import cv2
path="D:\=shubas.png"
src = cv2.imread(path)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow(window_name, image)
cv2.waitkey(5)
                   
