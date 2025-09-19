from flask import Flask, request, jsonify, render_template_string
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load trained model and label encoder
model = joblib.load("model.pkl")
le = joblib.load("label_encoder.pkl")
@app.route("/", methods=["GET"])
def home():
    return "Flask server is running!"

# HTML form for browser
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

# Home route
@app.route("/", methods=["GET"])
def home():
    return render_template_string(html_form, prediction=None)

# Form POST route
@app.route("/predict_form", methods=["POST"])
def predict_form():
    try:
        species = request.form["species"]
        count = float(request.form["count"])
        length_cm = float(request.form["length_cm"])

        # Encode species
        species_encoded = le.transform([species])[0]

        X = [[species_encoded, count, length_cm]]
        prediction = model.predict(X)[0]

        return render_template_string(html_form, prediction=int(prediction))
    except Exception as e:
        return f"Error: {str(e)}"

# API route for JSON POST
@app.route("/predict", methods=["POST"])
def predict_api():
    try:
        data = request.json
        species = data["species"]
        count = data["count"]
        length_cm = data["length_cm"]

        species_encoded = le.transform([species])[0]
        X = [[species_encoded, count, length_cm]]
        prediction = model.predict(X)[0]

        return jsonify({"predicted_size_class": int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
