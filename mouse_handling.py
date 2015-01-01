import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i] #list all events
print events

#mouse callback function
def draw_circle(event, x,y,flags,param):
    #if event == cv2.EVENT_LBUTTONDBLCLK: #left mouse double click event
    if event == cv2.EVENT_LBUTTONDOWN: #left mouse click down
        cv2.circle(img,(x,y),60,(255,0,0),1) #solid circle drawn

#create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')#create window
cv2.setMouseCallback('image',draw_circle)#bind function to window

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

 
        
