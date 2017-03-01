# Tutorial 10 : Using HSV to identify specific color

import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

while True :
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# set intial limits to be [0,0,0] and [255,255,255] for light and dark respectively
	light_blue = np.array([110, 100, 100])
	dark_blue = np.array([150,255,255])

	# inRange() method sets the value 1 for all the indices if the indices in 1st nparray is in range of the two given values
	mask = cv2.inRange(hsv, light_blue, dark_blue)
	res = cv2.bitwise_and(frame, frame, mask = mask)

	cv2.imshow('frame', frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)

	if cv2.waitKey(1) & 0xFF == ord('q') :
		break

cv2.destroyAllWindows()
cap.release()