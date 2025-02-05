#main.py

from fastapi import FastAPI, Request
from urllib.parse import parse_qs
from fastapi.middleware.cors import CORSMiddleware

import json

app = FastAPI(debug=True)

app.add_middleware(CORSMiddleware, allow_origins=["*"]) # Allow GET requests from all origins


@app.get("/")
async def root():
    return {"message": "Hello Worl1111d"}

@app.get("/api/")
async def api_data(request: Request):
    q_params = parse_qs(request.url.query, keep_blank_values=True)
    marks_list = []
    keyname_list = []
    json_dict = '' 
    d = dict((k, v if len(v)>1 else v[0]) 
                for k, v in q_params.items())

    with open('q-vercel-python.json') as f:
      json_dict = json.load(f)

    #for i in json_dict:
      #for keyname in d['name']:
      for keyname in d['name']:
        for i in json_dict:
          if i['name'] == keyname:
            keyname_list.append(keyname)
            marks_list.append(i['marks'])

    response_dict = { "marks" : marks_list}    
       
    return response_dict


