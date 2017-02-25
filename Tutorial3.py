# Tutorial 3 : Displaying a video from a file stored locally

import cv2
import numpy

print("Enter video filename")
filename = raw_input()

cap = cv2.VideoCapture(filename)

while True : 
	ret, frame = cap.read()
	if ret == False : 
		# video ended 
		break

	cv2.imshow('Movie Player', frame)

	if cv2.waitKey(25) & 0xFF == ord('q') :
		break

cap.release()
cv2.destroyAllWindows()