from capture import *
from db_print import *
from config import *
from request_printer import *
import time
import cv2
import json 

def get_stat_print(id):
    printer_id, name, printer_ip, camera_index = get_data(id)
    print(printer_ip + ":80")
    return print_status(printer_ip)


def create_photo(id):
    cam = Capture(id_camera=id)
    time.sleep(0.2)
    frame = cam.get_frame()
    if frame is None:
        return

    cv2.imwrite(photo_path, frame)

