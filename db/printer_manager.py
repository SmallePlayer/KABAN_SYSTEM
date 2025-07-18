import sqlite3
import sys
import os

# Добавляем родительскую директорию в путь для импорта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.db import (add_printer, get_all_printers, delete_printer, update_printer, update_printer_full, init_db, check_db_status)

def print_menu():
    print("\n--- Printer Management System ---")
    print("1. Add new printer")
    print("2. List all printers")
    print("3. Delete printer")
    print("4. Update printer")
    print("5. Exit")

def add_printer_console():
    print("\n--- Add New Printer ---")
    printer_id = input("Enter printer ID: ").strip()
    name = input("Enter printer name: ").strip()
    ip = input("Enter printer IP: ").strip()
    camera = input("Enter camera index: ").strip()

    try:
        camera_int = int(camera)
        if add_printer(printer_id, name, ip, camera_int):
            print("Printer added successfully!")
        else:
            print("Failed to add printer (printer with this ID may already exist)")
    except ValueError:
        print("Error: Camera index must be a number")

def list_printers():
    printers = get_all_printers()
    print("\n--- Registered Printers ---")
    for idx, printer in enumerate(printers, 1):
        print(f"{idx}. ID: {printer['id']}")
        print(f"   Name: {printer['name']}")
        print(f"   IP: {printer['ip']}")
        print(f"   Camera: {printer['camera']}")
        print("-" * 30)

def delete_printer_console():
    printer_id = input("Enter printer ID to delete: ").strip()
    if delete_printer(printer_id):
        print("Printer deleted successfully!")
    else:
        print("Printer not found or deletion failed")

def update_printer_console():
    printer_id = input("Enter printer ID to update: ").strip()
    
    printers = get_all_printers()
    printer_exists = any(p['id'] == printer_id for p in printers)
    
    if not printer_exists:
        print(f"Printer with ID {printer_id} not found!")
        return
    
    print("\n--- Update Printer ---")
    print("Which field do you want to update?")
    print("1. Name")
    print("2. IP Address")
    print("3. Camera Index")
    print("4. Update multiple fields")
    
    choice = input("Select option: ").strip()
    
    if choice == "1":
        new_name = input("Enter new name: ").strip()
        if update_printer(printer_id, 'name', new_name):
            print("Name updated successfully!")
        else:
            print("Failed to update name")
    
    elif choice == "2":
        new_ip = input("Enter new IP address: ").strip()
        if update_printer(printer_id, 'ip', new_ip):
            print("IP address updated successfully!")
        else:
            print("Failed to update IP address")
    
    elif choice == "3":
        new_camera = input("Enter new camera index: ").strip()
        try:
            camera_int = int(new_camera)
            if update_printer(printer_id, 'camera', camera_int):
                print("Camera index updated successfully!")
            else:
                print("Failed to update camera index")
        except ValueError:
            print("Error: Camera index must be a number")

    elif choice == "4":
        print("\n--- Update Multiple Fields ---")
        print("Leave field blank to keep current value")
        
        new_name = input("Enter new name: ").strip()
        new_ip = input("Enter new IP: ").strip()
        new_camera = input("Enter new camera index: ").strip()
        
        # Преобразуем пустые строки в None
        name = new_name if new_name else None
        ip = new_ip if new_ip else None
        camera = int(new_camera) if new_camera else None

        
        if update_printer_full(printer_id, name, ip, camera):
            print("Printer updated successfully!")
        else:
            print("Failed to update printer")
    
    else:
        print("Invalid option")

def main():
    # Инициализируем базу данных
    print("Initializing database...")
    if init_db():
        print("Database initialized successfully!")
    else:
        print("Failed to initialize database!")
        return
    
    # Проверяем состояние БД
    print("\nChecking database status...")
    check_db_status()
    
    while True:
        print_menu()
        choice = input("Select option: ").strip()
        
        if choice == "1":
            add_printer_console()
        elif choice == "2":
            list_printers()
        elif choice == "3":
            delete_printer_console()
        elif choice == "4":
            update_printer_console()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option, try again")

if __name__ == "__main__":
    main()