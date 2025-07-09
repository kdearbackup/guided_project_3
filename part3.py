import pickle
import pandas as pd

filename = 'trained_model.pkl'

# Open the file in read-binary mode and load the model
with open(filename, 'rb') as file:
    model = pickle.load(file)

print("Model loaded successfully")

parquet_file = 'troop_movements.parquet'
data = pd.read_parquet(parquet_file)

print("Data loaded successfully")
predictions = model.predict(data)

print("Predictions made successfully")

