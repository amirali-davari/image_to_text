# This file converts a video into frame images and saves them in a folder called "frames"
VIDEO_PATH = r"./bad_apple.mp4"

import cv2

vid = cv2.VideoCapture(VIDEO_PATH)

count, success = 0, True
while success:
    success, image = vid.read()
    if success: 
        cv2.imwrite(f"frames/frm{count}.jpg", image)
        count += 1

vid.release()