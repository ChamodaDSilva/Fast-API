from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app=FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool=True#if client send this its taken, otherwise get the default

@app.get("/")
def root():
    return{"message":"H"}


@app.get("/data")
def data_get():
    return{"data":"chamoda de silva"}

@app.post("/createposts")
def create_post(new_post:Post):
    print(new_post)
    return{"new_post":f"title {new_post.title} content: {new_post.content}"}


