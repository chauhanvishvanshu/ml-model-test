# CMLRE Marine Data Platform — Demo

This project is a simple **end-to-end ML web app** that predicts the **size class of fish** based on species, count, and length.  
It has:
- A **Flask backend** (serves the ML model as an API).
- A **Frontend (HTML/JS/CSS)** (simple UI to send requests).
- A **training script / notebook** to retrain the model.

---

## 📂 Project Structure

cmlre_full_project/
│── README.md
│── requirements.txt
│── analysis.ipynb # Jupyter notebook (exploration & training)
│── cmlre_biodiversity_data_sample.csv
│
├── backend/
│ ├── app.py # Flask API
│ ├── train_model.py # Train model script
│ ├── model.pkl # Trained DecisionTree model
│ └── label_encoder.pkl # Label encoder for species
│
└── frontend/
├── index.html # UI (form to submit data)
├── style.css
└── script.js

yaml
Copy code

---

## 🚀 Quick Start

### 1. Create environment and install dependencies
```bash

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Linux/Mac

pip install -r requirements.txt

⚠️ Note: The model was trained with scikit-learn 1.1.3.
If you face errors loading model.pkl, install the exact version:


pip install scikit-learn==1.1.3

2. Run the Flask backend
bash

python backend/app.py

This starts the server at:
👉 http://127.0.0.1:5000/

3. Open the frontend
Open frontend/index.html in your browser.

Fill the form with species, count, and length.

Click Predict → you’ll see the predicted size class.

4. API usage (optional)
You can call the backend directly:

python
Copy code
import requests

url = "http://127.0.0.1:5000/predict"
data = {"species": "FishA", "count": 10, "length_cm": 20.0}

res = requests.post(url, json=data)
print(res.json())
Example output:

json
Copy code
{"predicted_size_class": 2}
🏋️ Retraining the Model
To retrain with your own dataset:

Replace cmlre_biodiversity_data_sample.csv with your dataset.
It must have:

species (string)

count (int)

length_cm (float)

size_class (int label)

Run:

bash
Copy code
python backend/train_model.py
This will:

Train a new DecisionTree model.

Save updated model.pkl and label_encoder.pkl inside backend/.

Restart the Flask server to use the new model.

✅ Notes
If you input a species not present in training data, backend will return an error (Unknown species).

For demo purposes, species list in index.html is hardcoded. You can extend it to fetch dynamically from backend.

The Jupyter notebook analysis.ipynb shows training & exploration steps.

✨ Future Improvements
Add /species endpoint to serve species list for dropdown.

Improve frontend UI.

Add retrain button in frontend that calls /train.

🔧 Requirements
Python 3.8+

Flask

scikit-learn (1.1.3 recommended)

pandas, joblib