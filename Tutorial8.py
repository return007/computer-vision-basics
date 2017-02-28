# Tutorial 8 : Image superimposition (put 1 image over another)

import cv2
import numpy as np 

img1 = cv2.imread("./images/Tutorial7/in_1.jpg", cv2.IMREAD_COLOR)
img2 = cv2.imread("./images/Tutorial8/in_1.jpg", cv2.IMREAD_COLOR)
# we need to superimpose img2 over img1

rows, cols, zaxis = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img2gray, 240, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img_bg = cv2.bitwise_and(roi,roi,mask = mask)
img_fg = cv2.bitwise_and(img2, img2, mask = mask_inv)

res = cv2.add(img_fg, img_bg)

img1[0:rows, 0:cols] = res

cv2.imshow('img2gray',img2gray)
cv2.imshow('mask',mask)
cv2.imshow('img_bg',img_bg)
cv2.imshow('img_fg',img_fg)
cv2.imshow('res',res)
cv2.imshow('Final Image after superimposition', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()