# Import Modules
import cv2
import imutils
import numpy as np
from au import four_point_transform

# Read Image
image = cv2.imread('img.jpg')

ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image , height = 500)

# convert image to gray
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

# Blur Image
blurred = cv2.GaussianBlur(gray , (5,5) , 0)

# Show border
edged  = cv2.Canny(blurred , 75  , 200)
cv2.imshow('Edged' , edged)
cv2.waitKey(0)

# Grab Countours
cnts = cv2.findContours(edged.copy() , cv2.RETR_LIST , cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts , key=cv2.contourArea, reverse = True)

for c in cnts:
    peri = cv2.arcLength(c , True)
    approx = cv2.approxPolyDP(c , 0.04 * peri , True)
    if len(approx) == 4:
        finalCnt = approx
        break
cv2.drawContours(image , [finalCnt] , -1 , (0,255,0)  , 2)
cv2.imshow("Outline" , image)
cv2.waitKey(0)

zoom = four_point_transform(orig , finalCnt.reshape(4, 2) * ratio)
cv2.imshow("Zoom" , zoom)
cv2.waitKey(0)
