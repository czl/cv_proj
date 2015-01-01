import numpy as np
import cv2

cap = cv2.VideoCapture(0) #capture video source 0

while(cap.isOpened()): #when video capture is set
    ret, frame = cap.read()
    if ret:
        frame1 = cv2.flip(frame,0) #flip over x axis
        frame2 = cv2.flip(frame,1) #flip over y axis (mirror)

        cv2.imshow('orig', frame)
        cv2.imshow('mirror', frame2)
        cv2.imshow('flipped', frame1)
        if cv2.waitKey(1) & 0xFF == ord('q'): #if press 'q'
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
