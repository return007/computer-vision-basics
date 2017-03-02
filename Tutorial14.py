# Tutorial 14 : Image resizing (scaling) and 

import cv2
import numpy as np 

img = cv2.imread("./images/Tutorial14/in.jpg",cv2.IMREAD_COLOR)

# fx, fy  are multipliers
resizeimg = cv2.resize(img, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_LINEAR)

cv2.imshow('img',img)
cv2.imshow('resizeimg',resizeimg)

cv2.waitKey(0)
cv2.destroyAllWindows()