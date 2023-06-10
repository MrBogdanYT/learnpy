import cv2
import imutils
import numpy as np


# Camera in timp real = 0
# Video incarcat = punem unde e / numele
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Cannot open camera!')
    exit()
while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot Recive Frames!")
        break
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    cv2.imshow("Frame", gray)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
