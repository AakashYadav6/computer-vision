import cv2
import numpy as np

#reading an iamge from computer and taking dimensions
img = cv2.imread("/home/aakash/Desktop/project/python_files/test.png")
rows,cols = img.shape[:2]

#kernal blurring using filter2D()
kernal_25 = np.ones((25,25),np.float32) / 625.0
output_kernal = cv2.filter2D(img,-1,kernal_25)
#box filter and blur function 
output_blur = cv2.blur(img,(25,25))
output_box = cv2.boxFilter(img,-1,(5,5),normalize=False)

#gaussian blur mean,variance,standard deviation
output_gaus = cv2.GaussianBlur(img,(5,5),0)

#median blur (reduction of noise) kernal value 1 only
output_med = cv2.medianBlur(img,5)


#bilateral filtering (Reduction of noise  + preserving the edges)
output_bil = cv2.bilateralFilter(img,5,6,6)

cv2.imshow('kernal blur',output_kernal)
cv2.imshow('blur() output',output_blur)
cv2.imshow('box filter',output_box)
cv2.imshow('gaussian blur',output_gaus)
cv2.imshow('median blur',output_med)
cv2.imshow('bilateralFilter',output_bil)
cv2.waitKey()