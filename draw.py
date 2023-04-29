# Import Packages
import cv2
import imutils

# Load Image
image = cv2.imread("download.jpg")
(h,w,d) = image.shape
print(h,w,d)

# Display Image
cv2.imshow("Image" , image)
cv2.waitKey(0)


# Extract ROI 
#image[startY:endY , startX:endX]
roi = image[10:200 , 30:50]
cv2.imshow("ROI" , roi)
cv2.waitKey(0)

# Resize Image with OpenCV
resized = cv2.resize(image , (200,200))
cv2.imshow("OpenCV resize" , resized)
cv2.waitKey(0)

# Resize Image with Imutils
resized = imutils.resize(image , width=300)
cv2.imshow("Imutils resize" , resized)
cv2.waitKey(0)

# Rotate Image
rotated = imutils.rotate(image , 45)
cv2.imshow("Rotated Imutils" , rotated)
cv2.waitKey(0)

# Rotate image without cropping
rotated = imutils.rotate_bound(image , 45)
cv2.imshow("Rotated Imutils" , rotated)
cv2.waitKey(0)

# Apply a Gaussian Blur
blurred = cv2.GaussianBlur(image , (11 , 11) , 0)
cv2.imshow("Blurred Image" , blurred)
cv2.waitKey(0)

# Draw a Rectangle surrounding the face
output = image.copy()
cv2.rectangle(output , (300 , 10) , (500 , 200) , (0 , 0 ,255) , 2)
cv2.imshow("Drawn" , output)
cv2.waitKey(0)

# Draw a circle
output = image.copy()
cv2.circle(output, (50 , 50), 10, (0 , 0 , 255), thickness=1, lineType=8, shift=0)
cv2.imshow("Circle drawn" , output)
cv2.waitKey(0)

# Draw a line
output = image.copy()
cv2.line(output, (50, 150), (60, 70), (0, 255, 0), thickness=2)
cv2.imshow("Line drawn" , output)
cv2.waitKey(0)

# MrBogdan @ 2023
