from fastapi import FastAPI
from fastapi.params import Body

app=FastAPI()

@app.get("/")
def root():
    return{"message":"H"}


@app.get("/data")
def data_get():
    return{"data":"chamoda de silva"}

@app.post("/createposts")
def create_post(payload:dict=Body()):#get the body and convert to a dictionery named payload
    
    return{"new_post":f"title {payload['title']} content: {payload['content']}"}