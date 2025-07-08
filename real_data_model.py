import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('troop_movements_1m.csv')

df['unit_type'] = df['unit_type'].replace('invalid_unit', 'unknown') 

df['unit_type'] = df['unit_type'].fillna(method='ffill')

df.to_parquet('troop_movements.parquet', engine='pyarrow')

