import cv2
import imutils
import numpy as np

green = np.uint8([[[0,255,0]]])
hsv_green = cv2.cvtColor(green , cv2.COLOR_BGR2HSV)

print(hsv_green)