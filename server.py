from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import uvicorn
from db.db import *
from bot.db_bot.fun_add_bot import print_all_printer
from Core.core import create_photo

app = FastAPI()

app.mount("/frontEnd/static", StaticFiles(directory="frontEnd/static"), name="static")
templates = Jinja2Templates(directory="frontEnd/templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

@app.get("/", response_class=HTMLResponse)
def start(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": "Привет от FastAPI!"}
    )

@app.get("/all_printers")
def read_all_printer():
    printers = get_all_printers()
    return printers

@app.get("/printers/{id}/")
def read_simple_printer(id: int):
    return simple_printer(id)

@app.get("/printers/{id}/image")
def get_image_printer(id: int):
    path = create_photo(id)
    image_path = Path(path)

    if not image_path.exists():
        raise HTTPException(status_code=404, detail="Image not found")

    return Response(
        content=image_path.read_bytes(),
        media_type="image/jpeg"  # или "image/png"
    )

def simple_printer(id):
    printers = get_all_printers()
    simple_printer = printers[id]
    return simple_printer






if __name__ == "__main__":
    uvicorn.run("server:app", reload=True)