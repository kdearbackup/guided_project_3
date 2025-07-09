import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('troop_movements.csv')

# Empire or Resistance Dataframe Creation
empireOrResistanceDf = pd.DataFrame({"empire_or_resistance": [], "count": []})
empireCount = 0
resistanceCount = 0

#group by 'homeworld' and count occurances
homeworld_counts = df.groupby('homeworld').size().reset_index(name='count')
#Print grouping
print(homeworld_counts)

is_resistance_list = []
# Iterate through rows in Dataframe
for index, row in df.iterrows():
    if row['empire_or_resistance'] == 'empire':
        is_resistance_list.append(False)
        empireCount += 1
        #print(f"Index: {index}, unit_id: {row['unit_id']}, empire_or_resistance: {row['empire_or_resistance']}")
    else:
        resistanceCount += 1
        is_resistance_list.append(True)


# Add row to DataFrame (stuff after the = sign is the important part)
empireOrResistanceDf.loc[len(empireOrResistanceDf)] = ["empire", empireCount]
empireOrResistanceDf.loc[len(empireOrResistanceDf)] = ["resistance", resistanceCount]
print(empireOrResistanceDf)

# Unit dataframe stuff
unit_counts = df['unit_type'].value_counts()
unitTypeDf = unit_counts.to_frame()
unitTypeDf.columns = ['count'] 
unitTypeDf = unitTypeDf.reset_index() 
unitTypeDf = unitTypeDf.rename(columns={'index': 'unit type'})

# Adding is_resistance column to original dataframe
df['is_resistance'] = is_resistance_list

print(df)

# Create a countplot
sns.countplot(x='is_resistance', data=df)

# Display the plot
plt.show()

#print(df)



