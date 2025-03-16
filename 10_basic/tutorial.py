import cv2
#DEFAULT MODE CHANNEL ORDER IS BGR IN COLOR MODE 
 
#image =cv2.imread('test.png',cv2.IMREAD_COLOR)
#image =cv2.imread('test.png',cv2.IMREAD_GRAYSCALE)
image =cv2.imread('test.png',cv2.IMREAD_UNCHANGED)
cv2.imshow('test image', image)

cv2.waitKey(5000)
