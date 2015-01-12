import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('beach.jpg',0)
edges = cv2.Canny(img,150,170)

cap = cv2.VideoCapture(0)

##if cap:
##    ret, frame = cap.read()
##
##cap.release()
##frame = frame[:,:,::-1] #convert BGR to RGB
##frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) #convert RGB to grayscale
###cv2.imshow('gray',frame_gray)
##
###gaussian thresh holding
##th = cv2.adaptiveThreshold(frame_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
##plt.subplot(223),plt.imshow(th,'gray')
##plt.title('gaussian'),plt.xticks([]),plt.yticks([])
##
###canny edge detection
##edges_frame = cv2.Canny(frame,30,50)
##plt.subplot(221),plt.imshow(frame,cmap='gray')
##plt.title('orig'),plt.xticks([]),plt.yticks([])
##plt.subplot(222),plt.imshow(edges_frame,cmap='gray')
##plt.title('edge'),plt.xticks([]),plt.yticks([])
##
###Otsu's thresholding after Gaussian filtering
##blur = cv2.GaussianBlur(frame_gray,(3,3),0)
##ret,th1 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
##plt.subplot(224),plt.imshow(th1,'gray')
##plt.title('otsu'),plt.xticks([]),plt.yticks([])
##
##
##plt.show()


##live gaussian threshold
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        frame = frame[:,:,::-1] #BGR->RGB
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        gaus = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        cv2.imshow('gaussian', gaus)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
