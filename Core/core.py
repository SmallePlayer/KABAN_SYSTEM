from Core.capture import *
from db.db import *
from Core.config import *
from logger_config import setup_logger
from Core.test_request import emegency_stop
import time
import cv2
import os
import path


def emeg_stop(id: int):
    printer = get_printer(id)
    print(emegency_stop(printer['ip'] + ":80"))
    return printer["name"]

def create_photo(name: str):
    printer = get_printer_by_name(name)
    frame = get_frame(id_camera=int(printer[3]))
    time.sleep(0.2)

    photo_path = os.path.join(path.path_photo_rasp,
                f"photo_{printer[1]}.jpg")

    if frame is None:
        return

    cv2.imwrite(photo_path, frame)
    return photo_path