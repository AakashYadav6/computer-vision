import cv2

cap = cv2.VideoCapture("df.mp4")

if not cap.isOpened():
    print("Error: Cannot open video file")
    exit()
