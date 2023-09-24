import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("Videos/1.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)
