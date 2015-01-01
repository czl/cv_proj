import numpy as np
import cv2

#creating black image
#numpy.zeros(shape, dtype=float, order='C')
img = np.zeros((512,512,3), np.uint8)
##cv2.imshow('black', img)
##if cv2.waitKey(1) & 0xFF == ord('q'):
##    cv2.destroyAllWindows()
#draw diag blue line of thickness 5px
cv2.line(img,(0,0), (200,200), (255,0,0), 5)
print img
print 'line^'
#draw green rectangle
cv2.rectangle(img, (30,30), (400,200), (0,255,0), 3)

#draw red circle
#cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])-> None
cv2.circle(img, (230,230), 100, (0,0,255), -1) #-1 makes it filled

#draw ellipse, a half ellipse
#cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]) -> Non
#cv2.ellipse(img, box, color[, thickness[, lineType]]) -> None
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#draw polygon
#To draw a polygon, first you need coordinates of vertices.
#Make those points into an array of shape ROWSx1x2 where ROWS are
#number of vertices and it should be of type int32. Here we draw
#a small polygon of with four vertices in yellow color.
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

#write words
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,cv2.CV_AA)

print img
cv2.imshow('drawing', img)

if cv2.waitKey(5):
    cv2.destroyAllWindows()
