# Tutorial 4 : Capture video from Webcam and invert each frame and store it in form of a video

import cv2
import numpy

cap = cv2.VideoCapture(0)

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc is used to specify which video codec to use for storing the video file

fourcc = cv2.cv.CV_FOURCC(*'XVID')

out = cv2.VideoWriter("invert.avi", fourcc, 10, (640, 480))
# "invert.avi" : name of file
# fourcc : fourcc parameter
# 20.0 : frames per sec
# (640, 480) : dimension of video

while True :
	ret, frame = cap.read()
	
	if ret == False :
		break

	inv_frame = cv2.flip(frame, 1)
	out.write(inv_frame)
	cv2.imshow('invert video capture',inv_frame)
	if cv2.waitKey(20) & 0xFF == ord('q') :
		break

cap.release()
out.release()
cv2.destroyAllWindows()
