from flask import Flask, request, jsonify, render_template_string
import joblib, os

app = Flask(__name__)

# Load trained model and label encoder safely
try:
    model = joblib.load(os.path.join(os.path.dirname(__file__), "model.pkl"))
    le = joblib.load(os.path.join(os.path.dirname(__file__), "label_encoder.pkl"))
except Exception as e:
    model, le = None, None
    print(f"⚠️ Failed to load model/encoder: {e}")

# HTML form
html_form = """
<!doctype html>
<html>
<head><title>Fish Size Predictor</title></head>
<body>
<h2>Fish Size Class Predictor</h2>
<form method="post" action="/predict_form">
Species: <input type="text" name="species"><br><br>
Count: <input type="number" name="count"><br><br>
Length (cm): <input type="number" step="0.1" name="length_cm"><br><br>
<button type="submit">Predict</button>
</form>
{% if prediction is not none %}
<h3>Predicted Size Class: {{ prediction }}</h3>
{% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(html_form, prediction=None)

@app.route("/predict_form", methods=["POST"])
def predict_form():
    if not model or not le:
        return "❌ Model or encoder not loaded!"
    try:
        species = request.form["species"]
        count = float(request.form["count"])
        length_cm = float(request.form["length_cm"])

        if species not in le.classes_:
            return f"❌ Unknown species: {species}"

        species_encoded = le.transform([species])[0]
        prediction = model.predict([[species_encoded, count, length_cm]])[0]
        return render_template_string(html_form, prediction=int(prediction))
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/predict", methods=["POST"])
def predict_api():
    if not model or not le:
        return jsonify({"error": "Model or encoder not loaded!"}), 500
    try:
        data = request.json
        species, count, length_cm = data["species"], data["count"], data["length_cm"]

        if species not in le.classes_:
            return jsonify({"error": f"Unknown species: {species}"}), 400

        species_encoded = le.transform([species])[0]
        prediction = model.predict([[species_encoded, count, length_cm]])[0]
        return jsonify({"predicted_size_class": int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
