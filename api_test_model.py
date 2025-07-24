from flask import Flask, request, jsonify
import joblib
import numpy as np

# Créer l'application Flask
app = Flask(__name__)

# Charger le modèle entraîné
model = joblib.load(r"C:\Users\saido\Desktop\Analyse-de-Diab-te\logistic_regression_best_model.pkl")  # change selon ton fichier .pkl

# Optionnel : mapping cluster → risque
risk_mapping = {
    0: "Faible/Modéré",
    1: "Haut Risque",
    2: "Faible/Modéré",
    3: "Haut Risque",
    4: "Faible/Modéré"
}

@app.route("/")
def home():
    return "✅ API de prédiction de cluster de diabète prête."

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    try:
        # Extraire les valeurs dans le bon ordre
        features = [
            data['Glucose'],
            data['BMI'],
            data['Age'],
            data['DiabetesPedigreeFunction']
        ]

        # Conversion en tableau NumPy
        input_array = np.array(features).reshape(1, -1)

        # Prédiction
        cluster = model.predict(input_array)[0]
        risk = risk_mapping.get(cluster, "Inconnu")

        return jsonify({
            "cluster": int(cluster),
            "risk_category": risk
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Lancer le serveur
if __name__ == "__main__":
    app.run(debug=True)
