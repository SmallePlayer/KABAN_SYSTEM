# 🚀 Инструкции по развертыванию KABAN SYSTEM

## 📋 Предварительные требования

### Системные требования
- **ОС**: Windows 10/11, Linux (Ubuntu 20.04+), macOS
- **Python**: 3.8 или выше
- **RAM**: Минимум 2GB (рекомендуется 4GB+)
- **Дисковое пространство**: 1GB свободного места
- **Сеть**: Доступ к интернету и локальной сети с принтерами

### Оборудование
- **Камера**: USB веб-камера или IP-камера
- **Сеть**: Стабильное подключение к сети с 3D принтерами
- **Устройство**: ПК, ноутбук или сервер

## 🔧 Установка

### 1. Подготовка окружения

#### Windows
```bash
# Установка Python (если не установлен)
# Скачайте с https://www.python.org/downloads/

# Проверка версии Python
python --version

# Создание виртуального окружения
python -m venv kaban_env
kaban_env\Scripts\activate
```

#### Linux/macOS
```bash
# Установка Python
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Создание виртуального окружения
python3 -m venv kaban_env
source kaban_env/bin/activate
```

### 2. Установка зависимостей

```bash
# Обновление pip
pip install --upgrade pip

# Установка зависимостей
pip install -r requirements.txt
```

### 3. Настройка конфигурации

#### Настройка токена бота
1. Создайте бота в Telegram через @BotFather
2. Получите токен бота
3. Отредактируйте файл `Core/config.py`:

```python
BOT_TOKEN = "ваш_токен_бота_здесь"
```

#### Настройка путей (опционально)
Отредактируйте файл `Core/path.py` для вашей системы:

```python
# Для Windows
path_db_pc_home = 'C:/Users/ваш_пользователь/KABAN_SYSTEM/db/printer.db'
path_photo_pc_home = 'C:/Users/ваш_пользователь/KABAN_SYSTEM/photo'

# Для Linux
path_db_pc = '/home/ваш_пользователь/KABAN_SYSTEM/db/printer.db'
path_photo_pc = '/home/ваш_пользователь/KABAN_SYSTEM/photo'
```

### 4. Инициализация базы данных

```bash
# Проверка и инициализация БД
python check_db.py
```

## 🚀 Запуск системы

### Способ 1: Ручной запуск

#### Терминал 1 - Веб-сервер
```bash
# Активация виртуального окружения
source kaban_env/bin/activate  # Linux/macOS
# или
kaban_env\Scripts\activate     # Windows

# Запуск веб-сервера
python server.py
```

#### Терминал 2 - Telegram бот
```bash
# Активация виртуального окружения
source kaban_env/bin/activate  # Linux/macOS
# или
kaban_env\Scripts\activate     # Windows

# Запуск бота
python main.py
```

### Способ 2: Автоматический запуск

#### Windows - Создание bat файла
Создайте файл `start_system.bat`:

```batch
@echo off
echo Starting KABAN SYSTEM...
cd /d "C:\path\to\KABAN_SYSTEM"
call kaban_env\Scripts\activate
start "Web Server" python server.py
timeout /t 3
start "Telegram Bot" python main.py
echo System started successfully!
pause
```

#### Linux/macOS - Создание скрипта
Создайте файл `start_system.sh`:

```bash
#!/bin/bash
echo "Starting KABAN SYSTEM..."
cd /path/to/KABAN_SYSTEM
source kaban_env/bin/activate
python server.py &
sleep 3
python main.py &
echo "System started successfully!"
```

Сделайте скрипт исполняемым:
```bash
chmod +x start_system.sh
```

## 🔧 Настройка системы

### 1. Добавление принтеров

#### Через консольный менеджер
```bash
python db/printer_manager.py
```

Выберите опцию "1" и следуйте инструкциям:
- Введите ID принтера (например: "Н3")
- Введите название принтера (например: "3D Принтер Н3")
- Введите IP адрес принтера (например: "192.168.1.100")
- Введите индекс камеры (например: "0")

#### Через Telegram бота
1. Найдите вашего бота в Telegram
2. Отправьте команду `/start`
3. Выберите "Добавление принтера в базу данных"
4. Следуйте инструкциям бота

### 2. Настройка камер

#### Проверка доступных камер
```python
import cv2

# Проверка камеры с индексом 0
cap = cv2.VideoCapture(0)
if cap.isOpened():
    print("Камера 0 доступна")
    cap.release()
else:
    print("Камера 0 недоступна")

# Проверка камеры с индексом 1
cap = cv2.VideoCapture(1)
if cap.isOpened():
    print("Камера 1 доступна")
    cap.release()
else:
    print("Камера 1 недоступна")
```

#### Настройка индексов камер
- **0** - обычно встроенная камера ноутбука
- **1** - первая USB камера
- **2** - вторая USB камера
- И так далее...

### 3. Настройка сети

#### Проверка доступности принтеров
```bash
# Проверка доступности принтера по IP
ping 192.168.1.100

# Проверка HTTP доступа к принтеру
curl http://192.168.1.100:80/printer/objects/list
```

## 🔒 Безопасность

### 1. Настройка файрвола

#### Windows
```bash
# Разрешить входящие подключения на порт 8000
netsh advfirewall firewall add rule name="KABAN SYSTEM" dir=in action=allow protocol=TCP localport=8000
```

#### Linux
```bash
# Разрешить входящие подключения на порт 8000
sudo ufw allow 8000
```

### 2. Настройка HTTPS (опционально)

#### Получение SSL сертификата
```bash
# Установка certbot
sudo apt install certbot

# Получение сертификата
sudo certbot certonly --standalone -d your-domain.com
```

#### Настройка HTTPS в FastAPI
```python
# В server.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "server:app", 
        host="0.0.0.0", 
        port=8000,
        ssl_keyfile="/path/to/privkey.pem",
        ssl_certfile="/path/to/fullchain.pem"
    )
```

## 📊 Мониторинг

### 1. Логирование

#### Настройка логирования
Создайте файл `logging_config.py`:

```python
import logging
import os

# Создание папки для логов
os.makedirs('logs', exist_ok=True)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/kaban_system.log'),
        logging.StreamHandler()
    ]
)
```

#### Добавление в код
```python
import logging
logger = logging.getLogger(__name__)

# Использование
logger.info("Система запущена")
logger.error("Ошибка подключения к принтеру")
```

### 2. Мониторинг состояния

#### Проверка состояния системы
```bash
# Проверка процессов
ps aux | grep python

# Проверка портов
netstat -tulpn | grep 8000

# Проверка логов
tail -f logs/kaban_system.log
```

## 🔄 Обновление системы

### 1. Обновление кода
```bash
# Остановка системы
pkill -f "python server.py"
pkill -f "python main.py"

# Обновление кода
git pull origin main

# Обновление зависимостей
pip install -r requirements.txt --upgrade

# Перезапуск системы
python server.py &
python main.py &
```

### 2. Резервное копирование
```bash
# Создание резервной копии БД
cp db/printer.db db/printer_backup_$(date +%Y%m%d_%H%M%S).db

# Создание резервной копии фотографий
tar -czf photos_backup_$(date +%Y%m%d_%H%M%S).tar.gz photo/
```

## 🐛 Устранение неполадок

### Частые проблемы

#### 1. Ошибка "ModuleNotFoundError"
```bash
# Решение: Активируйте виртуальное окружение
source kaban_env/bin/activate  # Linux/macOS
kaban_env\Scripts\activate     # Windows
```

#### 2. Ошибка "Address already in use"
```bash
# Решение: Найдите и остановите процесс на порту 8000
lsof -ti:8000 | xargs kill -9  # Linux/macOS
netstat -ano | findstr :8000   # Windows
```

#### 3. Ошибка "Camera not found"
```bash
# Решение: Проверьте индекс камеры
python -c "import cv2; print([i for i in range(10) if cv2.VideoCapture(i).isOpened()])"
```

#### 4. Бот не отвечает
```bash
# Решение: Проверьте токен бота
python -c "from Core.config import BOT_TOKEN; print('Token:', BOT_TOKEN[:10] + '...')"
```

### Логи для диагностики

#### Проверка логов веб-сервера
```bash
tail -f logs/uvicorn.log
```

#### Проверка логов бота
```bash
tail -f logs/aiogram.log
```

## 📞 Поддержка

### Контакты
- **Email**: support@kaban-system.com
- **Telegram**: @kaban_support
- **GitHub Issues**: [Создать Issue](https://github.com/your-repo/issues)

### Информация для поддержки
При обращении в поддержку предоставьте:
1. Версию системы
2. Операционную систему
3. Логи ошибок
4. Скриншоты проблемы
5. Описание шагов для воспроизведения

---

**KABAN SYSTEM** - Инструкции по развертыванию  
Версия: 1.0  
Последнее обновление: 2024 