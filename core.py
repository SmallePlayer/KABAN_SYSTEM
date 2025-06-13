from capture import *
from db_print import *
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
    printer_id, name, printer_ip, camera_index, rele_pin = get_data(id)
    print(printer_ip + ":80")
    return print_status(printer_ip)

def edit_state_rele(state, id):
    printer_id, name, printer_ip, camera_index, rele_pin = get_data(id)
    return send_comand(state, rele_pin)

def create_photo(id):
    printer_id, name, printer_ip, camera_index, rele_pin = get_data(id)
    frame = get_frame(id_camera=int(camera_index))
    time.sleep(0.2)

    photo_path = os.path.join("photo", f"photo_{name}.jpg")

    if frame is None:
        return

    cv2.imwrite(photo_path, frame)
    return photo_path