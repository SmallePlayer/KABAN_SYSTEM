import requests
import time
from datetime import timedelta


def format_time(seconds):
    """Форматирование времени в ЧЧ:ММ:СС"""
    return str(timedelta(seconds=int(seconds)))

def get_printer_status(MOONRAKER_URL):
    try:
        # Собираем все данные за один запрос
        response = requests.get(
            f"{MOONRAKER_URL}/printer/objects/query?"
            "print_stats&"
            "virtual_sdcard&"
            "heater_bed&"
            "extruder"
        ).json()
        
        status = response['result']['status']
        print_stats = status['print_stats']
        virtual_sdcard = status['virtual_sdcard']
        
        # Основной статус
        state = print_stats['state']
        
        # Название файла
        filename = print_stats.get('filename', 'N/A').split('/')[-1]  # Только имя файла
        
        # Прогресс печати (в процентах)
        progress = virtual_sdcard.get('progress', 0) * 100
        
        # Временные параметры
        elapsed = print_stats.get('print_duration', 0)
        total_time = virtual_sdcard.get('total_duration', 0)
        
        # Расчет оставшегося времени
        remaining = (total_time - elapsed) if total_time > elapsed else 0
        
        # Температуры
        bed_temp = status['heater_bed']['temperature']
        nozzle_temp = status['extruder']['temperature']
        
        return {
            "state": state,
            "filename": filename,
            "progress": progress,
            "elapsed": elapsed,
            "elapsed_str": format_time(elapsed),
            "remaining": remaining,
            "remaining_str": format_time(remaining),
            "bed_temp": bed_temp,
            "nozzle_temp": nozzle_temp
        }
    except Exception as e:
        return {"error": str(e)}

# Цвета для консоли (опционально)
COLORS = {
    "printing": "\033[92m",  # Зеленый
    "paused": "\033[93m",    # Желтый
    "complete": "\033[94m",  # Синий
    "error": "\033[91m",     # Красный
    "reset": "\033[0m"       # Сброс
}

def print_status(id):
    data = get_printer_status(f"http://{id}:80")
    
    if "error" in data:
        print(f"Ошибка: {data['error']}")
    else:
        # Выбор цвета по статусу
        color = COLORS.get(data['state'].lower(), COLORS['reset'])
        
        print(
            f"{color}▶ Статус: {data['state'].upper()}{COLORS['reset']} | "
            f"Файл: {data['filename']}\n"
            f"  Прогресс: {data['progress']:.1f}% | "
            f"Затрачено: {data['elapsed_str']} | "
            f"Осталось: {data['remaining_str']}\n"
            f"  Сопло: {data['nozzle_temp']:.1f}°C | "
            f"Стол: {data['bed_temp']:.1f}°C\n"
            + "-"*50
        )
        return (
            f"{color}▶ Статус: {data['state'].upper()}{COLORS['reset']} | "
            f"Файл: {data['filename']}\n"
            f"  Прогресс: {data['progress']:.1f}% | "
            f"Затрачено: {data['elapsed_str']} | "
            f"Осталось: {data['remaining_str']}\n"
            f"  Сопло: {data['nozzle_temp']:.1f}°C | "
            f"Стол: {data['bed_temp']:.1f}°C\n"
            + "-"*50
        )
    
