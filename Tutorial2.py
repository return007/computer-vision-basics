# Tutorial 2 : Video capture and display using webcam 

import cv2
import numpy as np 
import matplotlib.pyplot as plt 

cap = cv2.VideoCapture(0)
# 0 means attached webcam
# 1 means USB camera

while True :
	ret, frame = cap.read()
	# ret is True or False, depending on the state of the frame read

	cv2.imshow('Video capture', frame)
	# display the image captured from the webcam

	key = cv2.waitKey(1)
	if key & 0xFF == ord('q') :
		# exit capturing mode when q is pressed
		break

cap.release()
#release the capture

cv2.destroyAllWindows()
# destroy all windows