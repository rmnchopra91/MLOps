import gradio as gr
import requests

# URL of the FastAPI backend
API_URL = "http://localhost:8000/predict"

# Function to make a request to FastAPI and return prediction
def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
    input_data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    response = requests.post(API_URL, json=input_data)
    print(f"{response.json()['prediction']} , type {type(response.json()['prediction'])}")
    output = {0: 'Iris Setosa', 1: 'Iris Versicolor', 2: 'Iris Virginica'}.get(response.json()["prediction"], 'Invalid')
    return output

# Create Gradio interface
interface = gr.Interface(
    fn=predict_iris,
    inputs=[
        gr.Number(label="Sepal Length"),
        gr.Number(label="Sepal Width"),
        gr.Number(label="Petal Length"),
        gr.Number(label="Petal Width"),
    ],
    outputs="text",
    title="Iris Flower Prediction",
    description="Enter flower measurements to predict the Iris species."
).launch(server_name="0.0.0.0", server_port=7860)