import uvicorn #ASGI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from cardios import Cardio
import numpy as np
import pickle
import joblib
from joblib import load
import pandas as pd


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


pickle_in = open("cardio_model.sav", "rb")
classifier1 = pickle.load(pickle_in)


@app.get('/')
def index():
    return {'message': 'Hello, World'}



@app.get('/{name}')
def get_name(name: str):
    return{'Welcome To My Medic Website': f'{name}'}

@app.post('/predict2')
def predict_cardio(data1:Cardio):
    data1 = data1.dict()
    Age = data1['Age']
    Female = data1['Female']
    Male = data1['Male']
    Height  =data1['Height']
    Weight =data1['Weight']
    BMI=data1['BMI']
    Systolicbloodpressure=data1['Systolicbloodpressure']
    Diastolicbloodpressure=data1['Diastolicbloodpressure']
    Cholesterol=data1['Cholesterol']
    Glucose=data1['Glucose']
    Smoking=data1['Smoking']
    Alcohol=data1['Alcohol']
    Physicalactivity=data1['Physicalactivity']

    #sc1=joblib.load('std_scaler.bin')
    #scaled_test_values = sc1.transform([[Age,Female,Male,Height,Weight,BMI,Systolicbloodpressure,Diastolicbloodpressure,Cholesterol,Glucose,Smoking,Alcohol,Physicalactivity]])

    #print(classifier.predict([[Age,Female,Male,Height,Weight,BMI,Systolicbloodpressure,Diastolicbloodpressure,Cholesterol,Glucose,Smoking,Alcohol,Physicalactivity]])
    prediction = classifier1.predict([[Age,Female,Male,Height,Weight,BMI,Systolicbloodpressure,Diastolicbloodpressure,Cholesterol,Glucose,Smoking,Alcohol,Physicalactivity]])

    if(prediction[0]>0.5):
        prediction= 1
    else:
        prediction= 0
    return {
        'prediction': prediction
    }



    
    

if __name__ =='__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)

#uvicorn app:app --reload
