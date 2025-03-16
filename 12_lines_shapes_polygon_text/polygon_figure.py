import cv2
import numpy as np 

#making a empty black canvas
#here canvas is of three layers
canvas = np.zeros((300,300,3))

#required points we need to join
pts = np.array([[250,5],[220,80],[280,80],[100,100]],np.int32)

#reshape the points to shape(number_vertex,1,2)
pts = pts.reshape((-1,1,2))

#draw this polygon
#here boolean True and False determine if the figure is closed
cv2.polylines(canvas,[pts],True,(0,255,0),3)

#showing the canvas
cv2.imshow('winname',canvas)
cv2.waitKey(20000)