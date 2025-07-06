import sys
import os
sys.path.append('.')

from db.db import add_printer, get_all_printers, check_db_status

print("=== Testing Printer Addition ===")

# Проверяем состояние БД
check_db_status()

# Добавляем тестовый принтер
print("\n=== Adding Test Printer ===")
success = add_printer("0", "Test Printer", "192.168.1.100", "0")
if success:
    print("Printer added successfully!")
else:
    print("Failed to add printer")

# Проверяем результат
print("\n=== Checking Result ===")
printers = get_all_printers()
if printers:
    for printer in printers:
        print(f"ID: {printer['id']}, Name: {printer['name']}, IP: {printer['ip']}, Camera: {printer['camera']}")
else:
    print("No printers found") 