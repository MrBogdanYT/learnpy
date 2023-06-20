import cv2
import os


# extract.py


cap = cv2.VideoCapture(0)


try:
    if not os.path.exists('data'):
        os.makedirs('data')
except:
    print("An error occured. Please try again later.")

currentframe = 0

while True:
    ret, frame = cap.read()
    
    if ret:
        name = './data/frame' + str(currentframe) + '.jpg'
        cv2.imwrite(name,frame)
        currentframe += 1
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
        
        # PRESS CTRL + C IN CMD TO STOP XDD


cap.release()
cv2.destroyAllWindows()
