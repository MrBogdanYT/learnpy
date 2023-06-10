import cv2
import imutils
import numpy as np

# Read Image
img = cv2.imread("img.jpg")

# Convert image to HSV
hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)

# Define Limits
lower = np.array([50,100,100])
upper = np.array([70,255,255])

# Mask
mask = cv2.inRange(hsv , lower , upper)

output = cv2.bitwise_and(img, img , mask , mask)
cv2.imshow('Images' , output)
cv2.waitKey(0)