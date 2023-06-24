import cv2
import imutils
import numpy as np
import os 
import time

from collections import deque

greenLower = (29, 86 , 6)
greenUpper = (64 , 255 , 255)
pts = deque(maxlen=64)

cap = cv2.VideoCapture(0)

time.sleep(2)

while True:
    ret, frame = cap.read()

    if not ret:
        break
    # Resize image, blur image and then convert it to HSV.
    frame = imutils.resize(frame , width = 600)
    blur = cv2.GaussianBlur(frame , (11, 11) , 0)
    hsv = cv2.cvtColor(blur , cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv , greenLower , greenUpper)
    mask = cv2.erode(mask , None , iterations=2)
    mask = cv2.dilate(mask , None , iterations=2)

    cnts = cv2.findContours(mask.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    center = None
    
    #cv2.imshow("mask" , mask)
    if len(cnts) > 0:
        # Extrage cel mai mare contur verde gasit
        c = max(cnts ,  key = cv2.contourArea)
        # Se extrag coordonatele cercului care incojoara conturul
        ((x , y) , radius) = cv2.minEnclosingCircle(c)
        # se calculeaza centrul conturului c
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]) , int(M["m01"] / M["m00"]) )
        # Daca raza e mai mare de 10 (variabil) 
        if radius > 10:
            # Desenam conturul cercului care inconjoara conturul gasit c
            cv2.circle(frame, (int(x) , int(y)) , int(radius) , (0 , 255,255) , 2)
            # Desenam centru conturului cercului c sunt forma unui cerc plin
            cv2.circle(frame , center , 5 , (0, 255, 255) , -1)
        
        pts.appendleft(center)
    # Parcurge lista de pts intermediare
    for i in range(1 , len(pts)):
        # Daca pts nu exista sari peste
        if pts[i-1] is None or pts[i] is None:
            continue
        # Altfel traseaza linia.
        cv2.line(frame , pts[i-1] , pts[i] , (0,255,255) , 5)
    cv2.imshow("frame" , frame)
        



    #cv2.imshow("Frame" , hsv)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
