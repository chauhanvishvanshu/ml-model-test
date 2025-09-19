# CMLRE Marine Data Platform — Full Project

This project contains a simple frontend, a Flask backend serving an ML model, and a Jupyter notebook used to train the model.

## Structure
```
cmlre_full_project/
│── README.md
│── requirements.txt
│── analysis.ipynb
│── model.pkl
│── cmlre_biodiversity_data_sample.csv
│
├── backend/
│   └── app.py
│
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js
```

## Quick start (local)
1. Create a virtual environment and install deps:
```bash
python -m venv venv
source venv/bin/activate    # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

2. Run the Flask API:
```bash
python backend/app.py
# By default it starts on http://127.0.0.1:5000
```

3. Open `frontend/index.html` in your browser (or serve it with any static server). Use the form to send data to the `/predict` endpoint.

## Notes
- The `analysis.ipynb` contains the training code and shows how `model.pkl` was created.
- `cmlre_biodiversity_data_sample.csv` is a small synthetic sample for demonstration. Replace it with your real dataset and re-train.
