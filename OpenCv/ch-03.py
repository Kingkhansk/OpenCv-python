from ctypes.wintypes import RGB
import cv2
import numpy as np

blank = np.zeros((500,500,3), np.uint8)
print(blank.shape)
# cv2.imshow('Blank', blank)
# cv2.waitKey(1000)

# 1. Paint the image a certain colour
blank[0:300, 0:400] = 255, 255, 255 # color in RGB as BGR (blue,green,red)
# cv2.imshow('Green', blank)
# cv2.waitKey(100)

# 2. Draw a line
cv2.line(blank, (0,250), (300,400), (0,0,250), thickness=3) #(img, starting point, end point, color , thickness)
cv2.imshow('Line', blank)
cv2.waitKey(1000)

# 3. Draw a Rectangle
cv2.rectangle(blank, (250,250), (500,500), (0,255,0), 2) #thickness in -ve fill the shape
cv2.rectangle(blank, (0,0), (250,250), (0,255,0), 2)
cv2.imshow('Rectangle', blank)
cv2.waitKey(100)

# 4. Draw A circle
cv2.circle(blank, (125,125), 100, (0,0,255), thickness=-1) #(img,center,radius,color,thickness)
cv2.imshow('Circle', blank)
cv2.waitKey(10)

# 5. Write text
cv2.putText(blank, 'Hello,', (10,225), cv2.FONT_HERSHEY_PLAIN, 1.7, (0,255,0), 2) #(img,text,SP,font,scale,color)
cv2.imshow('Text', blank)
cv2.waitKey(1000)