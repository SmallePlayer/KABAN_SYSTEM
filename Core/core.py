from Core.capture import *
from db.db import *
from Core.config import *
from Core.request_printer import *
from logger_config import setup_logger
from Core.uart_rele import *
import logging
import time
import cv2
import os


def get_stat_print(id):
    printer = get_printer(id)
    print(printer['pi'] + ":80")
    return print_status(printer['pi'] + ":80")

def edit_state_rele(state, id):
    printer = get_printer(id)
    return send_comand(state, printer['rele_pin'])

def create_photo(id):
    printer = get_printer(id)
    frame = get_frame(id_camera=int(printer[3]))
    time.sleep(0.2)

    photo_path = os.path.join("/home/main_server/KABAN_SYSTEM/photo",
                f"photo_{printer[1]}.jpg")

    if frame is None:
        return

    cv2.imwrite(photo_path, frame)
    return photo_path