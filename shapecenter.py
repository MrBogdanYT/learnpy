import cv2
import imutils

# Load Image 
image = cv2.imread("xd.png")

# Conver to GrayScale
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
cv2.imshow("Image" , gray)
cv2.waitKey(0)


# Blur it
blurred = cv2.GaussianBlur(gray,(5 , 5) , 0)
cv2.imshow("Blur" , blurred)
cv2.waitKey(0)

# Thresh it
thresh = cv2.threshold(blurred, 70 , 255 , cv2.THRESH_BINARY)[1]
cv2.imshow("Thresh" , thresh)
cv2.waitKey(0) 

# Find contours
cnts = cv2.findContours(thresh.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

output = image.copy()
# Loop Over cnts
for c in cnts:
    # compute center
    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX , cY = 0,0
    cv2.drawContours(image , [c] , -1 , (0,255,0) , 2)
    cv2.circle(image ,(cX , cY) , 7 , (255,255,255) , -1)
    cv2.putText(image , "center" , (cX -10 , cY - 10) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (255 , 255 , 255 ) , 2)

    cv2.imshow("Image", image)
    cv2.waitKey(0)
    
    
# MrBogdan @ 2023
