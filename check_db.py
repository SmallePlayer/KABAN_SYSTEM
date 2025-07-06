import sys
import os
sys.path.append('.')

from db.db import get_all_printers, check_db_status

print("=== Database Status ===")
check_db_status()

print("\n=== Printers in Database ===")
printers = get_all_printers()
if printers:
    for printer in printers:
        print(f"ID: {printer['id']}, Name: {printer['name']}, IP: {printer['ip']}, Camera: {printer['camera']}")
else:
    print("No printers found in database") 