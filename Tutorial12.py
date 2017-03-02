# Tutorial 12 : Morphological Transformation :: To remove noise from filters
# Two steps :: Erosion and Dilation

# Erosion means to remove the pixels that are different in a window size
# like if in 3x3 grid, 8 pixels are black expect the 9th one, so it will remove the 9th pixel

# Dilation is just the opposite of Erosion (increases the noise instead)

# Opening is to remove the false positives :: noises in the background
# Closing is to remove the false negatives :: in the object, black pixels

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

	kernal = np.ones((5,5), np.uint8)
	erosion = cv2.erode(mask, kernal, iterations = 1)
	dilation = cv2.dilate(mask, kernal, iterations = 1)

	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

	cv2.imshow('res',res)
	cv2.imshow('erosion',erosion)
	cv2.imshow('dilation',dilation)	
	cv2.imshow('opening',opening)
	cv2.imshow('closing',closing)

	k = cv2.waitKey(1) & 0xFF
	if k == ord('q') :
		break

cv2.destroyAllWindows()
cap.release()