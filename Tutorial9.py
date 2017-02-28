# Tutorial 9 : Example by self
# Video capture and image arithmetics revision

import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

width = cap.get(4)

img = cv2.imread('./images/Tutorial9/cloud.png',cv2.IMREAD_COLOR)
img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
img_fg = cv2.bitwise_and(img, img, mask = mask_inv)

rows, cols, zaxis = img.shape

x = 0
y = 0

while True :
	ret, frame = cap.read()

	nf = frame[x:x+rows, y:y+cols]	

	img_bg = cv2.bitwise_and(nf, nf, mask = mask)
	res = cv2.add(img_fg, img_bg)

	frame[x:x+rows,y:y+cols] = res

	cv2.imshow('Demo',frame)
	if cv2.waitKey(1) & 0xFF == ord('q') :
		break

	y = y + 5

	if y+cols >= width :
		y = 0

cap.release()
cv2.destroyAllWindows()