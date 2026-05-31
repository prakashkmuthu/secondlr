from sklearn.linear_model import LinearRegression
import pandas as pd
import joblib

# Read dataset
df = pd.read_csv("data.csv")

# Inputs (all columns except target)
X = df.drop(columns=["target"])

# Output column
y = df["target"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained and saved successfully!")