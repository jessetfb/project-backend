
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get('/Properties')
def get_properties():
    return{'name': 'lifestyle heights'}