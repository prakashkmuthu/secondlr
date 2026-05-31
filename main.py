from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

class InputData(BaseModel):
    experience: float

@app.get("/")
def home():
    return {"message": "Linear Regression API is running"}

@app.post("/predict")
def predict(data: InputData):
    input_data = [[data.experience]]
    prediction = model.predict(input_data)

    return {
        "experience": data.experience,
        "prediction": prediction[0]
    }