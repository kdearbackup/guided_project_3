import pandas as pd
import matplotlib.pyplot as plt
from model import exported_model, exported_features_encoded
import pickle

# Assuming 'model' is your trained machine learning model
importances = exported_model.feature_importances_

# Assuming 'X_encoded' is your DataFrame with encoded features
feature_importances = pd.DataFrame({
    'Feature': exported_features_encoded.columns,
    'Importance': importances
})

# Sort the DataFrame by importance
feature_importances = feature_importances.sort_values(by='Importance', ascending=False)

model = exported_model
with open('trained_model.pkl','wb')as file:
    pickle.dump(model,file)
print("Model saved to trained_model.pkl")

# Plot the feature importances
plt.figure(figsize=(10, 6))
plt.bar(feature_importances['Feature'], feature_importances['Importance'])
plt.title('Feature Importances')
plt.xlabel('Feature')
plt.ylabel('Importance')
plt.xticks(rotation=90)
plt.show()


