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
    return response.json()["prediction"]

# Create Gradio interface
interface = gr.Interface(
    fn=predict_iris,
    inputs=[
        gr.inputs.Number(label="Sepal Length"),
        gr.inputs.Number(label="Sepal Width"),
        gr.inputs.Number(label="Petal Length"),
        gr.inputs.Number(label="Petal Width")
    ],
    outputs="text",
    title="Iris Flower Prediction",
    description="Enter flower measurements to predict the Iris species."
)

if __name__ == "__main__":
    interface.launch()
