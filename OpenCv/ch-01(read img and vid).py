import cv2
# read image
img = cv2.imread("Resources/img/pn1.jpg")
cv2.imshow("Name", img)
cv2.waitKey(1000) # 1000 = 1s
# read video
vid  = cv2.VideoCapture("Resources/video/v2.mp4")
while True:
    isTrue, frame = vid.read()
    # if cv2.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv2.imshow('Video', frame)
        if cv2.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

vid.release()
cv2.destroyAllWindows()
