import cv2
import numpy

image =cv2.imread('test.png')

#translation matrix
matrix= numpy.float32([[1,0,100],[0,1,100]])


#applying the translation matrix to the image
translated = cv2.warpAffine(image,matrix,(image.shape[1]+100,image.shape[0]+100))


#showing the image
cv2.imshow('translation',translated)
cv2.imwrite("opencv_translation_image.jpg", translated)

print("Image saved as opencv_translation_image.jpg")
if(cv2.waitKey()==ord('q')):
	cv2.destroyAllWindows()
