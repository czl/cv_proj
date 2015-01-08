import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('beach.jpg',0)
edges = cv2.Canny(img,150,170)

cap = cv2.VideoCapture(0)

if cap:
    ret, frame = cap.read()

cap.release()
frame = frame[:,:,::-1] #convert BGR to RGB
frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) #convert RGB to grayscale
cv2.imshow('gray',frame_gray)

#gaussian thresh holding
th = cv2.adaptiveThreshold(frame_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
plt.subplot(223),plt.imshow(th,'gray')
plt.title('gaussian'),plt.xticks([]),plt.yticks([])

#canny edge detection
edges_frame = cv2.Canny(frame,30,50)
plt.subplot(221),plt.imshow(frame,cmap='gray')
plt.title('orig'),plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.imshow(edges_frame,cmap='gray')
plt.title('edge'),plt.xticks([]),plt.yticks([])

##plt.subplot(121),plt.imshow(img,cmap = 'gray')
##plt.title('orig img'),plt.xticks([]),plt.yticks([])
##plt.subplot(122),plt.imshow(edges,cmap = 'gray')
##plt.title('edge img'), plt.xticks([]),plt.yticks([])

plt.show()

