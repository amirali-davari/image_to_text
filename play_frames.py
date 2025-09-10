# This file plays the frames stored in "frames" folder.
# To watch the playing video, open output.txt (Visual Studio Code recommended)
# To generate frames, use vid_to_frame.py
VIDEO_FPS = 30
VIDEO_LEN_SECONDS = 218

import image_to_text
import cv2
import time
from pynput import keyboard

def on_key(key):
        if key == keyboard.Key.space:
            print('Playing...')
            b = time.time()
            delta = time.time() - b
            while delta < VIDEO_LEN_SECONDS:
                delta = time.time() - b
                img = cv2.resize(cv2.imread(f'frames/frm{round(delta*VIDEO_FPS)}.jpg'), (45, 34)).tolist()
                image_to_text.save_to_file(image_to_text.image_to_text(img))
                time.sleep(0.1)
            exit()

listener = keyboard.Listener(on_press=on_key)
listener.start()
listener.join()