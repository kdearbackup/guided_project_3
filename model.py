import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('troop_movements.csv')

# Select features and target variable
features = df[['homeworld','unit_type']]
target = df['empire_or_resistance']

#encode categorical features

features_encoded = pd.get_dummies(features)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features_encoded, target, test_size=0.2, random_state=42)

# Initialize the DecisionTreeClassifier
model = DecisionTreeClassifier()


#Fit the motel to the training data
model.fit(X_train,y_train)

#Make predictions
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
report = classification_report(y_test,y_pred)

print(f'Accuracy: {accuracy}')
print('Classification Report: ')
print(report)

exported_model = model
exported_features_encoded = features_encoded