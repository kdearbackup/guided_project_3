import pandas as pd
df = pd.read_csv('troop_movements.csv')

# Empire or Resistance Dataframe Creation
empireOrResistanceDf = pd.DataFrame({"empire_or_resistance": [], "count": []})
empireCount = 0
resistanceCount = 0

# Iterate through rows in Dataframe
for index, row in df.iterrows():
    if row['empire_or_resistance'] == 'empire':
        empireCount += 1
        #print(f"Index: {index}, unit_id: {row['unit_id']}, empire_or_resistance: {row['empire_or_resistance']}")
    else:
        resistanceCount += 1

# Add row to DataFrame (stuff after the = sign is the important part)
empireOrResistanceDf.loc[len(empireOrResistanceDf)] = ["empire", empireCount]
empireOrResistanceDf.loc[len(empireOrResistanceDf)] = ["resistance", resistanceCount]

print(empireOrResistanceDf)