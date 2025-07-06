#!/usr/bin/env python3
"""
Скрипт для запуска printer_manager из корневой директории проекта
"""

import sys
import os

# Добавляем текущую директорию в путь
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Импортируем и запускаем printer_manager
from db.printer_manager import main

if __name__ == "__main__":
    main() 