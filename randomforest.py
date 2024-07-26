import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load the labeled data
data = pd.read_csv('labeled_utilization.csv')

# Feature selection: selecting 'cpu' and 'ram' columns
X = data[['cpu', 'ram']]
y = data['label']

# Encode labels
y = y.map({'L': 0, 'M': 1, 'H': 2})

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Predict on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))

# Save the trained model
model_path = 'random_forest_model.joblib'
joblib.dump(rf_model, model_path)
print(f"Trained model saved to {model_path}")