import cv2
import imutils
import numpy as np

image = cv2.imread("sherlock.jpeg")
cv2.imshow("Original Image" , image)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2] , dtype = 'uint8')
cv2.circle(mask , (1050,250) , 200 , 255 , -1)


masked = cv2.bitwise_and(image,mask)
cv2.imshow("Masked" , masked)
cv2.waitKey(0)
