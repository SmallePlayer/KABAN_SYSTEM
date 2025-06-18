import cv2
import time


def get_frame(id_camera):
    cap = cv2.VideoCapture(id_camera)
    time.sleep(0.5)
    for _ in range(5):
        cap.grab()

        ret, frame = cap.read()

        if ret:
            cap.release()
            return frame
        else:
            print("None: ret")
            return frame



