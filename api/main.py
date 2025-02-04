#main.py

from fastapi import FASTAPI

app = FastAPI()

@app.get("/")

def read_root():
  return {"message" : "Hello World!"}


