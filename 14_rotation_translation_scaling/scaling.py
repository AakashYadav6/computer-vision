#optical zoom moving the zoom lens
#digital zoom interpoling the pixels after acquiring it with the help of sensor

import cv2
import numpy as np 

image = cv2.imread('test.png')

image_sized = cv2.resize(image,(300,300))

#interpolation types --- linear, cubic ,area , nearest neigbour ,sinosodial

#Resizing the image using linear interpolation
image_re_linear = cv2.resize(image,None,fx=6.5,fy=6.5,interpolation=cv2.INTER_LINEAR)


#resizing the image using cubic interpolation
image_re_cubic = cv2.resize(image,None,fx=6.5,fy=6.5,interpolation=cv2.INTER_CUBIC)


cv2.imshow('linear',image_re_linear)
cv2.imshow('cubic',image_re_cubic)
cv2.imshow('original',image)
cv2.imwrite("opencv_image_re_linear_image.jpg", image_re_linear)
cv2.imwrite("opencv_image_re_cubic_image.jpg", image_re_cubic)
print("Image saved as opencv_image_re_linear_image.jpg")
print("Image saved as opencv_image_re_cubic_image.jpg")

if(cv2.waitKey()==ord('q')):
	cv2.destroyAllWindows()

