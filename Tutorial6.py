# Tutorial 6 : Image operations (basic) (Handling basic pixels and range of pixels)

import numpy as np 
import cv2

img = cv2.imread("./images/Tutorial6/in.jpg",cv2.IMREAD_COLOR)

# value of the pixel
print(img[44,44])

roi = img[150:200, 150:200] # Region of Interest
img[100:150,100:150] = [255,255,255]

cv2.imshow("Display Image", img)
cv2.destroyAllWindows()