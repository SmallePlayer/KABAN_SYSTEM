import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    # Форматтер для всех обработчиков
    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Обработчик для файла (общий для всех)
    file_handler = RotatingFileHandler(
        'combined.log',
        maxBytes=5*1024*1024,  # 5 MB
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    
    # Добавляем обработчик к корневому логгеру
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)