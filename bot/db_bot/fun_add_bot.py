from db.db import *

def print_all_printer():
    printers = get_all_printers()
    
    
    message_parts = []
    current_message = "📋 Список принтеров:\n\n"
    
    for idx, printer in enumerate(printers, 1):
        printer_info = (
            f"{idx}. {printer['name']}\n"
            f"ID: {printer['id']}\n"
            f"IP: {printer['ip']}\n"
            f"Камера: {printer['camera']}\n"
            f"Реле: {printer['rele_pin']}\n\n")
        
        # Проверяем, не превысит ли добавление лимит
        if len(current_message) + len(printer_info) > 4000:
            message_parts.append(current_message)
            current_message = "📋 Список принтеров (продолжение):\n\n" + printer_info
        else:
            current_message += printer_info
    
    # Добавляем последнюю часть
    message_parts.append(current_message)
    return message_parts