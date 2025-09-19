import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

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

# 7. Save model and label encoder INSIDE backend/
save_dir = os.path.dirname(__file__)
joblib.dump(model, os.path.join(save_dir, "model.pkl"))
joblib.dump(le, os.path.join(save_dir, "label_encoder.pkl"))

print("✅ Model and encoder saved inside backend/")
