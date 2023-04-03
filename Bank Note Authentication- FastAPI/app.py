#pip install fastapi uvicorn

#Importing libraries
import uvicorn #ASGI
from fastapi import FastAPI
from BankNote import BankNote
import numpy as np
import pandas as pd
import pickle


#create app object
app =FastAPI()

#Load the pickle model
model_in = open('model.pkl','rb')
classifier = pickle.load(model_in)

#Index route opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello World'}

#Routed with a single parameter opens automatically on http://127.0.0.1:8000/name
@app.get('/welcome')
def get_name(name:str):
    return {'Welcome to my Web Page': f'{name}'}


# Expose the prediction functionality, make a prediction from the 
# passed JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_banknote(data:BankNote):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']

    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if (prediction[0]>0.5):
        prediction="Fake Note"
    else:
        prediction = "It's Original"
    return {
        'prediction': prediction
    }
#Run the API with uvicorn -http://127.0.0.1:8000

if __name__ == '__main__':
    uvicorn.run(app, host ='127.0.0.1', port=8000)

#Run the file in the anaconda prompt 
#uvicorn filename:objectname --reload
#uvicorn app:app --reload

# Swagger - http://127.0.0.1:8000/docs
# Swagger - http://127.0.0.1:8000/redocs


