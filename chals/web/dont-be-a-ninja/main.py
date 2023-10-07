from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

from templating import NinjaTemplate

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# loading a template from a file — nothing to see here
with open('templates/ninja.template', 'r') as f:
    ninja_file_contents = f.read()

@app.get("/")
async def home(request: Request):
    return FileResponse('templates/home.html')

@app.get("/ninja", response_class=HTMLResponse)
async def ninja(request: Request, name: str, power: str):
    print('hit')
    # why does this look vulnerable to template injection??
    return NinjaTemplate(templates.env, ninja_file_contents).render(
        name=name, power=power)
