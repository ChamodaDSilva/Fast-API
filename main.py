from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return{"message":"H"}


@app.get("/data")
def data_get():
    return{"data":"chamoda de silva"}