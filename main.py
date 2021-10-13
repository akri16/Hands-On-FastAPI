import uvicorn

if __name__ == '__main__':
    uvicorn.run("jinja.app:app", port=8000, reload=False)


