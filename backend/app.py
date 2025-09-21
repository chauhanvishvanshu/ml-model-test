from flask import Flask, request, jsonify, send_from_directory
import joblib, os

# Tell Flask where the frontend lives (../frontend from backend/)
app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), "../frontend"),
    static_url_path=""
)

# Load trained model and label encoder safely
try:
    model = joblib.load(os.path.join(os.path.dirname(__file__), "model.pkl"))
    le = joblib.load(os.path.join(os.path.dirname(__file__), "label_encoder.pkl"))
except Exception as e:
    model, le = None, None
    print(f"⚠️ Failed to load model/encoder: {e}")


# === FRONTEND ROUTES ===
@app.route("/")
def serve_index():
    """Serve the frontend index.html"""
    return send_from_directory(app.static_folder, "index.html")


# === API ROUTES ===
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


# Allow serving static files (style.css, script.js, etc.)
@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)


if __name__ == "__main__":
    app.run(debug=True)
