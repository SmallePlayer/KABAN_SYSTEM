import json
import logging
from logger_config import setup_logger

logger = logging.getLogger('db')

def read_data():
    with open('cam.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        logger.debug("read json")
    return data

def get_len_data():
    data = read_data()
    logger.debug(f" len data: {len(data)}")
    return len(data)

def get_data(target_id):
    data = read_data()

    found_data = None

    for datas in data:
        if datas['id'] == target_id:
            found_data = datas
            break
        
    if found_data:  
        id = found_data['id']  
        name = found_data['name']
        printer_ip = found_data['ip']
        camera = found_data['camera']
        rele_pin = found_data['rele_pin']

        logger.info(f"id {id} | name {name} | ip {printer_ip} | camera index {camera}")
        return id, name, printer_ip, camera, rele_pin
    else:
        logger.info(f"Данные для ID {target_id} не найдены")
        return None, None, None, None