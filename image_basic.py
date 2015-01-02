##NOTE!!! img[y,x] selection is backwards!!

# ['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON',
# 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY',
# 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP',
# 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP',
# 'EVENT_MOUSEMOVE', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN',
# 'EVENT_RBUTTONUP']

import numpy as np
import cv2

img = cv2.imread('beach.jpg')

#get image type
print img.dtype

cv2.imshow('image', img)

a = [-1,-1]
select = False #left mouse button not down
cp = img[0:0, 0:0]
delta = [-1,-1]

def handle(event,x,y,flags,param):
    print 'x:%d -- y:%d'%(x,y)
    global select,a,cp,delta
    print flags
    print event
    bgr = img[y,x] ##NOTE!!! img[y,x] selection is backwards!!
##    print bgr[0],bgr[1],bgr[2]
    #start select
    if not(select) and flags == (cv2.EVENT_FLAG_CTRLKEY + cv2.EVENT_FLAG_LBUTTON):
        print "start selecting"
        a = [x,y]
        select = True
    #done selecting
    elif select and flags == cv2.EVENT_FLAG_CTRLKEY and event == cv2.EVENT_LBUTTONUP:
        print "correct"
        select = False
        #draw white rectangle around selection
        cp = img[a[0]:x, a[1]:y]
        delta = [x-a[0],y-a[1]]
        print "delta: %d,%d" %(delta[0],delta[1])
        cv2.rectangle(img,(a[0],a[1]),(x,y), (255,255,255),2)
        cv2.imshow('image',img)
    elif flags == cv2.EVENT_FLAG_ALTKEY and event == cv2.EVENT_LBUTTONUP:
        print "delta: %d,%d" %(delta[0],delta[1])
    
        

cv2.setMouseCallback('image',handle)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
