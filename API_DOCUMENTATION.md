# 📚 API Документация KABAN SYSTEM

## 🌐 Обзор API

KABAN SYSTEM предоставляет REST API для управления 3D принтерами. API построен на FastAPI и поддерживает JSON формат данных.

### Базовый URL
```
http://localhost:8000
```

### Аутентификация
В текущей версии API не требует аутентификации. Для продакшена рекомендуется настроить JWT токены.

## 📋 Endpoints

### 🏠 Главная страница

#### GET /
Возвращает главную страницу веб-интерфейса.

**Параметры:** Нет

**Ответ:**
- **Тип:** HTML
- **Описание:** Главная страница с дашбордом принтеров

**Пример запроса:**
```bash
curl http://localhost:8000/
```

---

### 🖨️ Управление принтерами

#### GET /all_printers
Возвращает список всех принтеров в базе данных.

**Параметры:** Нет

**Ответ:**
```json
[
  {
    "id": "Н3",
    "name": "3D Принтер Н3",
    "ip": "192.168.1.100",
    "camera": "0"
  },
  {
    "id": "Слон",
    "name": "3D Принтер Слон",
    "ip": "192.168.1.101",
    "camera": "1"
  }
]
```

**Пример запроса:**
```bash
curl http://localhost:8000/all_printers
```

**Коды ответов:**
- `200 OK` - Успешное получение списка
- `500 Internal Server Error` - Ошибка сервера

---



### 📷 Управление фотографиями

#### GET /printer_photo/{printer_id}
Возвращает фотографию принтера.

**Параметры:**
- `printer_id` (string) - ID принтера

**Ответ:**
- **Тип:** Image (JPEG)
- **Описание:** Фотография принтера или дефолтное изображение

**Пример запроса:**
```bash
curl http://localhost:8000/printer_photo/Н3
```

**Коды ответов:**
- `200 OK` - Успешное получение фото
- `404 Not Found` - Фото не найдено

**Особенности:**
- Если фото принтера не найдено, возвращается дефолтное изображение
- Поддерживает русские символы в именах файлов
- Автоматическое кэширование браузером

---

#### POST /update_printer_photo/{printer_id}
Обновляет фотографию принтера, делая новый снимок с камеры.

**Параметры:**
- `printer_id` (string) - ID принтера

**Тело запроса:** Нет

**Ответ:**
```json
{
  "success": true,
  "message": "Photo updated for printer 3D Принтер Н3",
  "path": "C:/Users/pes/PycharmProjects/KABAN_SYSTEM/photo/photo_Н3.jpg"
}
```

**Пример запроса:**
```bash
curl -X POST http://localhost:8000/update_printer_photo/Н3
```

**Коды ответов:**
- `200 OK` - Фото успешно обновлено
- `404 Not Found` - Принтер не найден
- `500 Internal Server Error` - Ошибка создания фото

**Особенности:**
- Автоматически определяет камеру принтера из БД
- Применяет специальные настройки для разных принтеров (например, переворачивание для "Слон")
- Сохраняет фото в папку `photo/`

---



## 🔧 Статические файлы

### CSS и JavaScript
```
GET /static/css/styles.css
GET /static/js/script.js
```

### Фотографии
```
GET /photo/photo_Н3.jpg
GET /photo/photo_Слон.jpg
```

## 📊 Модели данных

### Printer Model
```json
{
  "id": "string",      // Уникальный ID принтера
  "name": "string",    // Название принтера
  "ip": "string",      // IP адрес принтера
  "camera": "string"   // Индекс камеры
}
```

### Error Response
```json
{
  "detail": "string"   // Описание ошибки
}
```

### Success Response
```json
{
  "success": true,
  "message": "string",
  "path": "string"     // Путь к файлу (опционально)
}
```

## 🚀 Примеры использования

### Python

#### Получение списка принтеров
```python
import requests

response = requests.get('http://localhost:8000/all_printers')
printers = response.json()

for printer in printers:
    print(f"Принтер: {printer['name']} (IP: {printer['ip']})")
```

#### Обновление фото принтера
```python
import requests

printer_id = "Н3"
response = requests.post(f'http://localhost:8000/update_printer_photo/{printer_id}')

if response.status_code == 200:
    result = response.json()
    print(f"Фото обновлено: {result['message']}")
else:
    print(f"Ошибка: {response.json()['detail']}")
```

#### Получение фото принтера
```python
import requests

printer_id = "Н3"
response = requests.get(f'http://localhost:8000/printer_photo/{printer_id}')

if response.status_code == 200:
    with open(f'printer_{printer_id}.jpg', 'wb') as f:
        f.write(response.content)
    print("Фото сохранено")
```

### JavaScript

#### Получение списка принтеров
```javascript
async function getPrinters() {
    try {
        const response = await fetch('http://localhost:8000/all_printers');
        const printers = await response.json();
        
        printers.forEach(printer => {
            console.log(`Принтер: ${printer.name} (IP: ${printer.ip})`);
        });
    } catch (error) {
        console.error('Ошибка:', error);
    }
}
```

#### Обновление фото принтера
```javascript
async function updatePrinterPhoto(printerId) {
    try {
        const response = await fetch(`http://localhost:8000/update_printer_photo/${printerId}`, {
            method: 'POST'
        });
        
        if (response.ok) {
            const result = await response.json();
            console.log(`Фото обновлено: ${result.message}`);
        } else {
            const error = await response.json();
            console.error(`Ошибка: ${error.detail}`);
        }
    } catch (error) {
        console.error('Ошибка:', error);
    }
}
```

### cURL

#### Получение всех принтеров
```bash
curl -X GET "http://localhost:8000/all_printers" \
     -H "Accept: application/json"
```

#### Обновление фото принтера
```bash
curl -X POST "http://localhost:8000/update_printer_photo/Н3" \
     -H "Content-Type: application/json"
```

#### Получение фото принтера
```bash
curl -X GET "http://localhost:8000/printer_photo/Н3" \
     -o printer_photo.jpg
```

## 🔒 Безопасность

### Рекомендации

1. **Ограничение доступа**
   ```python
   # В server.py
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["http://localhost:3000"],  # Только разрешенные домены
       allow_credentials=True,
       allow_methods=["GET", "POST"],
       allow_headers=["*"],
   )
   ```

2. **Rate Limiting**
   ```python
   from slowapi import Limiter, _rate_limit_exceeded_handler
   from slowapi.util import get_remote_address
   from slowapi.errors import RateLimitExceeded
   
   limiter = Limiter(key_func=get_remote_address)
   app.state.limiter = limiter
   app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
   
   @app.get("/all_printers")
   @limiter.limit("10/minute")
   def read_all_printer(request: Request):
       # ...
   ```

3. **Аутентификация (планируется)**
   ```python
   from fastapi.security import HTTPBearer
   
   security = HTTPBearer()
   
   @app.get("/all_printers")
   async def read_all_printer(token: str = Depends(security)):
       # Проверка токена
       # ...
   ```

## 🐛 Обработка ошибок

### Стандартные коды ошибок

| Код | Описание |
|-----|----------|
| 200 | OK - Успешный запрос |
| 400 | Bad Request - Неверный запрос |
| 404 | Not Found - Ресурс не найден |
| 500 | Internal Server Error - Ошибка сервера |

### Примеры ошибок

#### 404 - Принтер не найден
```json
{
  "detail": "Printer not found"
}
```

#### 500 - Ошибка создания фото
```json
{
  "detail": "Failed to create photo"
}
```

#### 404 - Фото не найдено
```json
{
  "detail": "Photo not found: [Errno 2] No such file or directory"
}
```

## 📈 Мониторинг API

### Логирование запросов
```python
import logging
import time
from fastapi import Request

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    logging.info(
        f"{request.method} {request.url.path} "
        f"- Status: {response.status_code} "
        f"- Time: {process_time:.3f}s"
    )
    
    return response
```

### Метрики
- Количество запросов в минуту
- Время отклика API
- Количество ошибок
- Популярные endpoints

## 🔄 Версионирование API

### Текущая версия: v1

Все текущие endpoints относятся к версии v1. В будущем планируется добавление версионирования:

```
GET /api/v1/all_printers
GET /api/v2/all_printers
```

## 📞 Поддержка API

### Контакты
- **Email**: api-support@kaban-system.com
- **Telegram**: @kaban_api_support
- **GitHub Issues**: [API Issues](https://github.com/your-repo/issues)

### Информация для поддержки
При обращении в поддержку API предоставьте:
1. Версию API
2. Endpoint, который вызывает проблему
3. Параметры запроса
4. Полный ответ сервера
5. Логи клиента

---

**KABAN SYSTEM** - API Документация  
Версия API: 1.0  
Последнее обновление: 2024 