# Tutorial 13 : Edge detection and gradient 
# Two techniques of edge detection : 
# 1. Sobel : different for x and y direction, first order derivatives, gradient based method, uses different kernels for x and y direction
# 2. Laplacian : only 1 kernel used, 2nd order derivative used, much sensitive to noise, 

# Canny edge detection 

import numpy as np 
import cv2

cap = cv2.VideoCapture(0)
while True :
	_, frame = cap.read()

	# apply edge detection after removal of noise only
	gaussian = cv2.GaussianBlur(frame, (15,15), 1)

	laplacian = cv2.Laplacian(frame, cv2.CV_64F)
	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 1)
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 1)

	canny = cv2.Canny(frame, 0, 255)
	# cv2.imshow('frame',frame)
	# cv2.imshow('laplacian',laplacian)
	# cv2.imshow('sobelx',sobelx)
	# cv2.imshow('sobely',sobely)
	cv2.imshow('canny',canny)


	k = cv2.waitKey(1)
	if k & 0xFF == ord('q') :
		break

cv2.destroyAllWindows()
cap.release()