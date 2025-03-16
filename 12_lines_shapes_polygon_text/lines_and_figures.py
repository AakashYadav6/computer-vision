import cv2
import numpy as np

#creating a canvas 500x500 three channels
canvas= np.zeros((500,500,3))

#drawing a line >>>>>  img,pt1,pt2,color,linethickness,line type-line4,line8,lineAA aliasing nad anti aliasing(transparance)
#line 4 and line 8 -- bresenham algo
#line AA -gausian filtering
#cv2.line(img,pt1,pt2,color)
cv2.line(canvas,(0,0),(100,100),(0,255,0),2,cv2.LINE_4)

cv2.line(canvas,(0,20),(120,120),(0,255,0),2,cv2.LINE_8)


#drawing a rectangle  diagonal points p1 and pt 2
cv2.rectangle(canvas,(200,200),(250,270),(0,0,255),-1)

#drawing a circle
cv2.circle(canvas,(250,250),10,(255,0,0),3)

#drawing an arrowed line
cv2.arrowedLine(canvas,(400,400),(500,500),(255,255,255),tipLength=0.3)

cv2.imshow('winname',canvas)
cv2.waitKey(20000)