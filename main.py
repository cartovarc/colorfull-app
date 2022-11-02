import os
import uvicorn

from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))


@app.get('/')
def index(request: Request):
    background_color = os.getenv("BACKGROUND_COLOR", "red")
    message = os.getenv("MESSAGE", "This is default message")

    return templates.TemplateResponse(
        'index.html',
        context={'request': request, 'background_color': background_color, "message": message}
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
