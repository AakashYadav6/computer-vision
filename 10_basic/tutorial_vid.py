import cv2

#0 for system camera or video file or online ip of camera or 1 for connected camera

cap= cv2.VideoCapture(0)
opened =cap.isOpened()

#codec coding scheme for writing and reading differet video format
#fourcc
fourcc = cv2.VideoWriter_fourcc(*'MJPG')


height =cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fps = cap.get(cv2.CAP_PROP_FPS)

print(height)
print(width)
print("Frames are {}".format(fps))

#VIDEO WRITER
out =cv2.VideoWriter('jj.avi',fourcc,fps,(int(width),int(height)))

if(opened):
   while(cap.isOpened()):
       ret, frame =cap.read()
       #ret boolen return whether frame is returned 0 will give error
       if(ret==True):
           cv2.imshow('aakashwin',frame)
           out.write(frame)
           if(cv2.waitKey(2)==27): #every two second check whether user is giving some input  esc value 27
              break
#video and memory release 
out.release()
cap.release()
cv2.destroyAllWindows()
