## drawing hollow rectangles and circles

import numpy as np
import cv2

drawing = False #true if mouse is pressed down
mode = "rect" #can toggle between different shapes
a = [-1,-1]

#mouse callback function
def draw(event, x,y, flags,param):
	global a,drawing,mode

	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		a = [x,y]
##	elif event == cv2.EVENT_MOUSEMOVE:
##		if drawing:
##			if mode == "rect":
##				cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
##			elif mode == "circle":
##				cv2.circle(img,(x,y),5,(0,0,255),-1)
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		if mode == "rect":
			cv2.rectangle(img,(a[0],a[1]),(x,y),(0,255,0),2)
		elif mode == "circle":
			b = [-1,-1]
			b = [x,y]
			c = np.square(np.subtract(a,b))
			radius = np.sqrt(c[0]+c[1])/2.0
			print radius
			center = np.divide((np.add(a,b)),2)
			print "center: (%s,%s)\nradius: %s" %(center[0],center[1],radius)
			print "np.rint(radius): %s" %np.rint(radius)
			cv2.circle(img,(int(center[0]),int(center[1])), int(radius),(0,0,255),2)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)

while 1:
	cv2.imshow('image',img)
	k = cv2.waitKey(1) & 0xFF
	if k == ord('m'):
		if mode == "rect":
			mode = "circle"
		elif mode == "circle":
			mode = "rect"
	elif k == ord('q'):
		break

cv2.destroyAllWindows()
