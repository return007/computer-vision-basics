# Tutorial 11 : After we have done with identification of specific color, we need to blur/smoothen the image (ie reduce noise)

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while True :
	_,frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# set intial limits to be [0,0,0] and [255,255,255] for light and dark respectively
	light_blue = np.array([110, 100, 100])
	dark_blue = np.array([150,255,255])

	mask = cv2.inRange(hsv, light_blue,dark_blue)
	res = cv2.bitwise_and(frame, frame, mask = mask)

	# Now Apply blur techniques (Low Pass Filters)
	# blur basically does is averages the pixel values taking neighbours also in consideration
	# 3 blurring techniques that are implemented here are : 
	# 1. GaussianBlur :: very easy, average value in the sliding window neighbourhood
	# 2. medianBlur   :: uses the median of all the pixels in the window
	# 3. bilateralBlur:: need to study

	# Image Filtering using Convolution2D

	average = cv2.blur(res, (10,10))
	gaussian = cv2.GaussianBlur(res, (15,15), 1)
	median = cv2.medianBlur(res, 5)
	bilateral = cv2.bilateralFilter(res, 9, 75, 75)

	cv2.imshow('res',res)
	cv2.imshow('average',average)
	cv2.imshow('gaussian',gaussian)	
	cv2.imshow('median',median)
	cv2.imshow('bilateral',bilateral)


	k = cv2.waitKey(1) & 0xFF
	if k == ord('q') :
		break

cv2.destroyAllWindows()
cap.release()