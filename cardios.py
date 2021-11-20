from pydantic import BaseModel

class Cardio(BaseModel):
    Age : float
    Female : float
    Male : float
    Height: float
    Weight : float
    BMI : float
    Systolicbloodpressure : float
    Diastolicbloodpressure: float
    Cholesterol : float
    Glucose: float
    Smoking : float
    Alcohol : float
    Physicalactivity: float
    