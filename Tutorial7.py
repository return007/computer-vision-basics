# Tutorial 7 : Basic Image Arithmetic (Addition of Images using +, add() and addWeighted() methods)
import cv2
import numpy as np 

img1 = cv2.imread("./images/Tutorial7/in_1.jpg",cv2.IMREAD_COLOR)
img2 = cv2.imread("./images/Tutorial7/in_2.jpg",cv2.IMREAD_COLOR)


# img1 = img1 / 2
# img2 = img2 / 2
add1 = img1 + img2

add2 = cv2.add(img1, img2)
# cv2.add() does simple pixel addition
# example [120, 200, 10] + [120, 100, 50] = [240, 255, 60]

cv2.imshow("Frame1",add1)
cv2.imshow("Frame2",add2)
cv2.waitKey(0)

if (np.array_equal(add1, add2)) :
	print("True")
else :
	print("False")

weighted = cv2.addWeighted(img1, 0.4, img2, 0.6, 0)
# weighted sum of images last parameter is gamma value

cv2.imshow("weighted",weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()