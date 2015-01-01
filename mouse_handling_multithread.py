import numpy as np
import cv2
import time #for python to try and get sleep to happen to delay inner ring
import thread
import threading

exitFlag = 0
num_clicks = 0

#thread class for click handling
class myThread(threading.Thread):
    def __init__(self,x,y):
        threading.Thread.__init__(self)
        self.x = x
        self.y = y
    def run(self):
        global num_clicks
        print "click%d" %num_clicks
        num_clicks += 1
        time.sleep(1)
        cv2.circle(img,(self.x,self.y),56,(200,200,200),2)
        cv2.imshow('image', img)
        time.sleep(1)
        cv2.circle(img,(self.x,self.y),53,(100,200,50),2)


events = [i for i in dir(cv2) if 'EVENT' in i] #list all events
print events

#mouse callback function
def draw_circle(event, x,y,flags,param):
    #if event == cv2.EVENT_LBUTTONDBLCLK: #left mouse double click event
    if event == cv2.EVENT_LBUTTONDOWN: #left mouse click down
        cv2.circle(img,(x,y),60,(255,0,0),1) #solid circle drawn
        cv2.imshow('image', img)
        myThread(x,y).start()
        
##        cv2.circle(img,(x,y),59,(12,88,200),1)

#create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')#create window
cv2.setMouseCallback('image',draw_circle)#bind function to window

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

