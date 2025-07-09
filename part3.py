import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

filename = 'trained_model.pkl'

# Open the file in read-binary mode and load the model
with open(filename, 'rb') as file:
    model = pickle.load(file)

print("Model loaded successfully")

parquet_file = 'troop_movements.parquet'
data = pd.read_parquet(parquet_file)

X = data[['homeworld', 'unit_type']]
X_encoded = pd.get_dummies(X)

print("Data loaded successfully")
predictions = model.predict(X_encoded)

print("Predictions made successfully")

data["predictions"] = predictions

print(data)

