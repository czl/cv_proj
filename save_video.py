import numpy as np
import cv2
import os

cap = cv2.VideoCapture(1) #capture video source 0

#determine video height, 4 CV_CAP_PROP_FRAME_HEIGHT
height = cap.get(4)
#determine video width, 3 CV_CAP_PROP_FRAME_WIDTH
width = cap.get(3)
#determine video frame rate, 5 CV_CAP_PROP_FPS
fps = cap.get(5)
#determine fourcc codec code 6 CV_CAP_PROP_FOURCC
fourcc = cap.get(6)
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#fourcc = cv2.cv.CV_FOURCC(*'DIVX')
#none of the codecs are available, so have to set on runtime
####necessary for writing
print fourcc
cap.set(5,30) #doesn't do anything
print cap.get(5)
fps = 22.0 #frame rate isn't constant, varies between 22-35
print fps
#cap.set(3,1024)
#cap.set(4,768)
print width
print height
if os.path.isfile('C:\Users\CL\Desktop\output.avi'):
    os.remove('C:\Users\CL\Desktop\output.avi')
out = cv2.VideoWriter('C:\Users\CL\Desktop\output.avi', -1, fps, (int(width),int(height)))
#out = cv2.VideoWriter('C:\Users\CL\Desktop\output.avi', -1, fps, (1024,768))
####

##while True:
##    start = cv2.getTickCount()
##    ret, frame = cap.read()
##    if cv2.waitKey(3) >= 0:
##        break
##    print cv2.getTickFrequency()/(cv2.getTickCount()-start)

while(cap.isOpened()): #when video capture is set
    ret, frame = cap.read()
    if ret:
        frame1 = cv2.flip(frame,0) #flip over x axis
        frame2 = cv2.flip(frame,1) #flip over y axis (mirror)

        cv2.imshow('orig', frame)
        cv2.imshow('mirror', frame2)
        cv2.imshow('flipped', frame1)

        #write orig video
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): #if press 'q'
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
