from capture import *
from db_print import *
from db_test import *
from config import *
from request_printer import *
from logger_config import setup_logger
from uart_rele import *
import logging
import time
import cv2
import json 
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

    photo_path = os.path.join("photo", f"photo_{printer[1]}.jpg")

    if frame is None:
        return

    cv2.imwrite(photo_path, frame)
    return photo_path