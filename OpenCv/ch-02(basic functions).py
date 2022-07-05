import imghdr
from turtle import shape
import cv2
# print(cv2.__version__)
img = cv2.imread("Resources/img/g1.jpg")
img1 = cv2.imread("Resources/img/pn1.jpg")
img2 = cv2.imread("Resources/img/g2.jpg")
cv2.imshow("lasd", img)
cv2.waitKey(1000)

# Converting to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(1000)

# Blur 
blur = cv2.GaussianBlur(gray, (7,7),0)
cv2.imshow('Blur', blur)
cv2.waitKey(1000)

# Edge Cascade
canny = cv2.Canny(img, 125, 175)
cv2.imshow('Canny Edges', canny)
cv2.waitKey(1000)

# Dilating the image
dilated = cv2.dilate(canny, (7,7), iterations=3)
cv2.imshow('Dilated', dilated)
cv2.waitKey(1000)

# Eroding
eroded = cv2.erode(canny, (7,7), iterations=3)
cv2.imshow('Eroded', eroded)
cv2.waitKey(1000)

# Resize
resized = cv2.resize(img1, (500,500), interpolation=cv2.INTER_CUBIC) #(width,height)
cv2.imshow('Resized', resized)
cv2.waitKey(1000)

# Cropping
cropped = img2[0:500, 0:500] #[Height , width]
cv2.imshow('Cropped', cropped)
cv2.waitKey(1000)