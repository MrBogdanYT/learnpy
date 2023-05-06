# Import Modules
import cv2
import imutils

# Import Image and Show it
image = cv2.imread("image.jpg")
cv2.imshow("Image" , image)
cv2.waitKey(0)

# Convert Image to Grayscale
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image" , gray)
cv2.waitKey(0)

# Edge detection to find outlines of objects
edged = cv2.Canny(gray , 30 , 150)
cv2.imshow("Edged" , gray)
cv2.waitKey(0)

# Threshold the Image
# All Pixel values < 255 => white
# All Pixel values > 255 => black
thresh = cv2.threshold(gray , 225 , 255 , cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Threshed" , thresh)
cv2.waitKey(0)

# Find Contours in the threshold image
cnts = cv2.findContours(thresh.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

output = image.copy()
# Loop Over cnts
for c in cnts:
    # Draw Each contour on the image
    cv2.drawContours(output,  [c] , -1 , (255 , 0 , 0) , 3)
    cv2.imshow("Contours" , output)
    cv2.waitKey(0)

# MrBogdan @ 2023
