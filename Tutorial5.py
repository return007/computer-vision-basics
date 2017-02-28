# Tutorial 5 : Basic shapes 

import cv2
import numpy as np 

img = np.zeros((512,512,3), np.uint8)

cv2.line(img, (0,0), (511, 511), (255,0,0), 5)
cv2.rectangle(img, (31,31), (490,490), (0,255,255), 2)
cv2.circle(img, (255,255), 50, (0,0,255), -100)
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

pts = np.array([[100,50],[200,300],[300,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),8)

cv2.imshow("Frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
