from fastapi import FastAPI
from fastapi.datastructures import UploadFile
from fastapi.param_functions import Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request, Form, File
from fastapi.staticfiles import StaticFiles

from jinja.schemas import AwesomeForm


app = FastAPI()
templating = Jinja2Templates(directory="jinja/templates")
app.mount("/static", StaticFiles(directory="jinja/static"), name="static")


@app.get('/')
def helloWorld() -> dict:
    return {"message": "Hello World"}


@app.get("/items/{id}", response_class=HTMLResponse)
async def readItem(id: str, request: Request):
    return templating.TemplateResponse("index.jinja", {
        "request": request, "id": id})


@app.get('/form', response_class=HTMLResponse)
def getForm(request: Request):
    return templating.TemplateResponse("basic-form.jinja", {
        "request": request})


@app.post('/form', response_class=HTMLResponse)
async def getForm(request: Request, username: str = Form(...),
                  password: str = Form(...), file: UploadFile = File(...)):

    print(f'username: {username}')
    print(f'password: {password}')
    content = await file.read()
    print(content)

    return templating.TemplateResponse("basic-form.jinja", {
        "request": request})


# @app.get('/awesome-form', response_class=HTMLResponse)
# def getForm(request: Request):
#     return templating.TemplateResponse("basic-form.jinja", {
#         "request": request})


# @app.post('/awesome-form', response_class=HTMLResponse)
# def getForm(request: Request,
#             form_data: AwesomeForm = Depends(AwesomeForm.as_form)):

#     print(form_data)

#     return templating.TemplateResponse("basic-form.jinja", {
#         "request": request})

