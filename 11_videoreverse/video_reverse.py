import cv2

cap= cv2.VideoCapture('df_fixed.mp4')

#properties of video
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(cap.get(cv2.CAP_PROP_FPS))
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

#INITIATIONG THE OUTPUT WRITER FOR VIDEO
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('reversed.avi',fourcc,fps,(width,height))


print("No. of frames are : {}".format(frames))
print("FPS is :{}".format(fps))

#we get the index of the last frame of the video file
frame_index = frames -1

if(cap.isOpened()):
	while(frame_index>=0):
		#we set the current frame position to last frame
		cap.set(cv2.CAP_PROP_POS_FRAMES,frame_index)
		ret,frame =cap.read()


		#resize the frame 
		#frame= cv2.resize(frame,(int(width*0.5),int(height*0.5)))
		frame= cv2.resize(frame,(height,width))

		#OPTIONAL : To show the reversing video
		#cv2.imshow('winname', frame)

		#writing the reversed video
		out.write(frame)

		#decrementing the frame index at each loop
		frame_index -= 1
		#Printing the progress
		if(frame_index%100==0):
			print(frame_index)
		# if(cv2.waitKey(2)==ord('q')):
		# 	break


out.release()
cap.release()
cv2.destroyAllWindows()
