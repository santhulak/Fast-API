#pip install fastapi uvicorn

#Importing libraries
import uvicorn #ASGI
from fastapi import FastAPI

#create app object
app =FastAPI()

#Index route opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello World'}

#Routed with a single parameter opens automatically on http://127.0.0.1:8000/name
@app.get('/welcome')
def get_name(name:str):
    return {'Welcome to my Web Page': f'{name}'}

#Run the API with uvicorn -http://127.0.0.1:8000

if __name__ == '__main__':
    uvicorn.run(app, host ='127.0.0.1', port=8000)

#Run the file in the anaconda prompt 
#uvicorn filename:objectname --reload
#uvicorn api:app --reload

# Swagger - http://127.0.0.1:8000/docs
# Swagger - http://127.0.0.1:8000/redocs


