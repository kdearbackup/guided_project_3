import pandas as pd

# Load the dataset
df = pd.read_csv('troop_movements.csv')
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 20)

# Apply pd.get_dummies to create one-hot encoded columns for 'homeworld'
data_numeric = pd.get_dummies(df, columns=['homeworld', 'timestamp', 'empire_or_resistance','unit_type'])

# Convert only boolean columns to integers (0 and 1)
for column in data_numeric.columns:
    if data_numeric[column].dtype == 'bool':
        data_numeric[column] = data_numeric[column].astype(int)

# Print the DataFrame to see the numeric representation
print(data_numeric)



