import sqlite3
import os


# Путь к базе данных (абсолютный путь)
current_dir = os.path.dirname(os.path.abspath(__file__))
db_name = os.path.join(current_dir, "printer.db")


def get_connection():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn

# Инициализация БД
def check_db_status():
    """Проверка состояния базы данных"""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='printers'")
            table_exists = cursor.fetchone() is not None
            
            if table_exists:
                cursor.execute("SELECT COUNT(*) FROM printers")
                count = cursor.fetchone()[0]
                print(f"Database status: OK")
                print(f"Table 'printers' exists: {table_exists}")
                print(f"Number of printers: {count}")
                return True
            else:
                print("Database status: Table 'printers' does not exist")
                return False
    except Exception as e:
        print(f"Database status error: {e}")
        return False

# Инициализация БД
def init_db():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS printers (id TEXT PRIMARY KEY, name TEXT NOT NULL, ip TEXT NOT NULL, camera TEXT NOT NULL)''')
            conn.commit()
            print(f"Database initialized successfully at: {db_name}")
            return True
    except Exception as e:
        print(f"Error initializing database: {e}")
        return False

# Добавление нового принтера
def add_printer(id, name, ip, camera):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO printers (id, name, ip, camera) VALUES (?, ?, ?, ?)''', (id, name, ip, camera))
            conn.commit()
            print(f"Successfully added printer: ID={id}, Name={name}, IP={ip}, Camera={camera}")
            return True
    except sqlite3.IntegrityError as e:
        print(f"Error: Printer with ID {id} already exists")
        return False
    except Exception as e:
        print(f"Error adding printer: {e}")
        return False

# Получение данных принтера по ID
def get_printer(target_id):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM printers WHERE id = ?", (target_id,))
            printer = cursor.fetchone()
            if printer:
                return (
                    printer['id'],
                    printer['name'],
                    printer['ip'],
                    printer['camera'],
                )
            return None
    except Exception as e:
        return None
    
def get_printer_by_name(target_name):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM printers WHERE name = ?", (target_name,))
            printer = cursor.fetchone()
            if printer:
                return (
                    printer['id'],
                    printer['name'],
                    printer['ip'],
                    printer['camera'],
                )
            return None
    except Exception as e:
        return None

# Получение количества принтеров
def get_printers_count():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM printers")
            return cursor.fetchone()[0]
    except Exception as e:
        return 0

# Получение списка всех принтеров
def get_all_printers():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM printers")
            printers = [dict(row) for row in cursor.fetchall()]
            print(f"Retrieved {len(printers)} printers from database")
            return printers
    except Exception as e:
        print(f"Error getting printers: {e}")
        return []

def delete_printer(target_id):
    try:
        with get_connection() as conn:
            if conn is None:
                print("Ошибка: Нет подключения к БД")
                # logger.error("Ошибка: Нет подключения к БД")
                return False
            cursor = conn.cursor()
            cursor.execute("DELETE FROM printers WHERE id = ?", (target_id,))
            conn.commit()
            return cursor.rowcount > 0
    except Exception as e:
        return False
    
def update_printer(target_id, field, new_value):
    try:
        # Проверяем допустимые поля для обновления
        allowed_fields = ['name', 'ip', 'camera']
        if field not in allowed_fields:
            return False
        
        with get_connection() as conn:
            cursor = conn.cursor()
            # Для числовых полей преобразуем значение
            if field in ['camera']:
                try:
                    new_value = int(new_value)
                except ValueError:
                    return False
            
            # Формируем SQL-запрос динамически
            query = f"UPDATE printers SET {field} = ? WHERE id = ?"
            cursor.execute(query, (new_value, target_id))
            conn.commit()
            
            if cursor.rowcount > 0:
                return True
            else:
                return False
    except Exception as e:
        return False

# НОВАЯ ФУНКЦИЯ: Полное обновление принтера
def update_printer_full(target_id, name=None, ip=None, camera=None):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            
            # Получаем текущие данные
            cursor.execute("SELECT * FROM printers WHERE id = ?", (target_id,))
            printer = cursor.fetchone()
            if not printer:
                return False
                
            # Обновляем только переданные значения
            update_fields = {}
            if name is not None:
                update_fields['name'] = name
            if ip is not None:
                update_fields['ip'] = ip
            if camera is not None:
                try:
                    update_fields['camera'] = int(camera)
                except ValueError:
                    return False
            
            # Формируем SQL-запрос
            if not update_fields:
                return False
                
            set_clause = ", ".join([f"{field} = ?" for field in update_fields])
            values = list(update_fields.values())
            values.append(target_id)
            
            query = f"UPDATE printers SET {set_clause} WHERE id = ?"
            cursor.execute(query, values)
            conn.commit()
            
            return True
    except Exception as e:
        return False

init_db()

