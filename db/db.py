import sqlite3
import Core.path as pt


db_name = pt.path_db_rasp


def get_connection():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row  # Для доступа к столбцам по имени
    return conn

# Инициализация БД
def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS printers (id TEXT PRIMARY KEY, name TEXT NOT NULL, ip TEXT NOT NULL, camera TEXT NOT NULL)''')
        conn.commit()
        # logger.info("Database initialized")

# Добавление нового принтера
def add_printer(id, name, ip, camera):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO printers (id, name, ip, camera) VALUES (?, ?, ?, ?, ?)''', (id, name, ip, camera))
            conn.commit()
            # logger.info(f"Added printer: ID={id}, Name={name}")
            return True
    except sqlite3.IntegrityError:
        # logger.error(f"Printer with ID {id} already exists")
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
        # logger.error(f"Error fetching printer: {str(e)}")
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
        # logger.error(f"Error fetching printer: {str(e)}")
        return None

# Получение количества принтеров
def get_printers_count():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM printers")
            return cursor.fetchone()[0]
    except Exception as e:
        # logger.error(f"Error counting printers: {str(e)}")
        return 0

# Получение списка всех принтеров
def get_all_printers():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM printers")
            return [dict(row) for row in cursor.fetchall()]
    except Exception as e:
        # logger.error(f"Error fetching printers: {str(e)}")
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
            # logger.info(f"Deleted printer: ID={target_id}")
            return cursor.rowcount > 0
    except Exception as e:
        # logger.error(f"Error deleting printer: {str(e)}")
        return False
    
def update_printer(target_id, field, new_value):
    try:
        # Проверяем допустимые поля для обновления
        allowed_fields = ['name', 'ip', 'camera']
        if field not in allowed_fields:
            # logger.error(f"Invalid field for update: {field}")
            return False
        
        with get_connection() as conn:
            cursor = conn.cursor()
            # Для числовых полей преобразуем значение
            if field in ['camera']:
                try:
                    new_value = int(new_value)
                except ValueError:
                    # logger.error(f"Invalid value for {field}: must be integer")
                    return False
            
            # Формируем SQL-запрос динамически
            query = f"UPDATE printers SET {field} = ? WHERE id = ?"
            cursor.execute(query, (new_value, target_id))
            conn.commit()
            
            if cursor.rowcount > 0:
                # logger.info(f"Updated printer {target_id}: {field} = {new_value}")
                return True
            else:
                # logger.warning(f"No printer found with ID {target_id}")
                return False
    except Exception as e:
        # logger.error(f"Error updating printer: {str(e)}")
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
                # logger.warning(f"No printer found with ID {target_id}")
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
                    # logger.error("Camera must be integer")
                    return False
            
            # Формируем SQL-запрос
            if not update_fields:
                # logger.warning("No fields to update")
                return False
                
            set_clause = ", ".join([f"{field} = ?" for field in update_fields])
            values = list(update_fields.values())
            values.append(target_id)
            
            query = f"UPDATE printers SET {set_clause} WHERE id = ?"
            cursor.execute(query, values)
            conn.commit()
            
            # logger.info(f"Updated printer {target_id}: {len(update_fields)} fields")
            return True
    except Exception as e:
        # logger.error(f"Error updating printer: {str(e)}")
        return False

# Инициализируем БД при импорте модуля


init_db()

