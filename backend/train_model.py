import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# 1. Load dataset
data = pd.read_csv("../cmlre_biodiversity_data_sample.csv")

# 2. Encode species column
le = LabelEncoder()
data["species_encoded"] = le.fit_transform(data["species"])

# 3. Define features (X) and target (y)
X = data[["species_encoded", "count", "length_cm"]]  # Input features
y = data["size_class"]                               # Target label

# 4. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train Decision Tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 6. Evaluate accuracy
accuracy = model.score(X_test, y_test)
print(f"✅ Model trained. Test accuracy: {accuracy:.2f}")

# 7. Save model and label encoder
joblib.dump(model, "model.pkl")
joblib.dump(le, "label_encoder.pkl")
print("✅ Model and encoder saved in backend/")
