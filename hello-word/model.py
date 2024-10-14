import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Train and save the model
def train_model():
    # Load Iris dataset
    X, y = load_iris(return_X_y=True)
    
    # Train RandomForest model
    model = RandomForestClassifier().fit(X, y)
    
    # Save the trained model
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Model saved as model.pkl")

# Load the model and make a prediction
def predict(test_data):
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    # Make prediction
    prediction = model.predict([test_data])
    print(f"Prediction for {test_data}: {prediction[0]}")

if __name__ == '__main__':
    train_model()  # Train and save the model
    
    # Example test data
    sample_data = [5.1, 3.5, 1.4, 0.2]
    predict(sample_data)  # Load the model and predict
