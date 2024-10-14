from fastapi import FastAPI
import pickle
from pydantic import BaseModel

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define input data schema
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Initialize FastAPI app
app = FastAPI()

# Define prediction endpoint
@app.post("/predict")
def predict(input_data: IrisInput):
    # Extract input features
    data = [[
        input_data.sepal_length, 
        input_data.sepal_width, 
        input_data.petal_length, 
        input_data.petal_width
    ]]
    # Make prediction
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}
