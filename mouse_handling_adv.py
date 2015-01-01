##
## simple drawing program like paint that has rectangle drawing
## and fat circular line drawing, using rectangle and circle functions
## to draw.
## using button down and button up and mouse tracking to draw

import numpy as np
import cv2

drawing = False #true if mouse is pressed down
mode = "rect" #can toggle between different shapes
ix,iy = -1,-1

#mouse callback function
def draw_circle(event, x,y, flags,param):
	global ix,iy,drawing,mode

	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix,iy = x,y
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing:
			if mode == "rect":
				cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
			elif mode == "circle":
				cv2.circle(img,(x,y),5,(0,0,255),-1)
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		if mode == "rect":
			cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
		elif mode == "circle":
			cv2.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

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
