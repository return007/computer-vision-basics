import cv2
import matplotlib.pyplot as plt 

def imageRead(filename) : 
	img = cv2.imread(filename, 0)
	return img

def displayImage(img) :
	cv2.imshow("Browser",img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def writeImage(img) :
	filename = "./images/Tutorial1/out.png"
	cv2.imwrite(filename, img)

print("Specify image path")
filename = raw_input()
img = imageRead(filename)
displayImage(img)
writeImage(img)