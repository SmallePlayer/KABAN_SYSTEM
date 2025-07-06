from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import uvicorn
from db.db import *
from Core.core import create_photo

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontEnd/static"), name="static")
app.mount("/photo", StaticFiles(directory="photo"), name="photo")
templates = Jinja2Templates(directory="frontEnd")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

@app.get("/", response_class=HTMLResponse)
def start(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.get("/all_printers")
def read_all_printer():
    printers = get_all_printers()
    return printers

@app.get("/printers/{id}/")
def read_printer(id_printer: int):
    return date_printer(id_printer)

@app.get("/printers/{id}/image")
def get_image_printer(id_printer: str):
    path_image = create_photo(id_printer)
    image_path = Path(path_image)

    if not image_path.exists():
        raise HTTPException(status_code=404, detail="Image not found")

    return Response(
        content=image_path.read_bytes(),
        media_type="image/jpeg"
    )

@app.get("/printer_photo/{printer_id}")
def get_printer_photo(printer_id: str):
    """Специальный маршрут для получения фото принтера с русскими именами"""
    try:
        photo_path = Path(f"photo/photo_{printer_id}.jpg")
        if not photo_path.exists():
            # Если фото не найдено, возвращаем дефолтное
            photo_path = Path("photo/photo_Н3.jpg")
        
        return Response(
            content=photo_path.read_bytes(),
            media_type="image/jpeg"
        )
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Photo not found: {e}")

@app.post("/update_printer_photo/{printer_id}")
def update_printer_photo(printer_id: str):
    """Обновление фото принтера через create_photo"""
    try:
        # Получаем принтер по ID
        printer = get_printer(printer_id)
        if not printer:
            raise HTTPException(status_code=404, detail="Printer not found")
        
        # Создаем новое фото используя name принтера
        photo_path = create_photo(printer[1])  # printer[1] - это name
        
        if photo_path:
            return {"success": True, "message": f"Photo updated for printer {printer[1]}", "path": photo_path}
        else:
            raise HTTPException(status_code=500, detail="Failed to create photo")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating photo: {str(e)}")

def date_printer(id_printer):
    printers = get_all_printers()
    simple_printer = printers[id_printer]
    return simple_printer



if __name__ == "__main__":
    uvicorn.run("server:app", reload=True)