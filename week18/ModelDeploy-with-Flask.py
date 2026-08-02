from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the model
with open("C:\\Users\\Talha\\Documents\\GitHub\\Fullstack-AI-BOOTCAMP-B-10\\predictive_maintenance_model.pkl", "rb") as f:
    model = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Parse the input data (sensor readings)
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)

        # Make predictions
        prediction = model.predict(features)
        #result = "Failure predicted" if prediction[0] == 1 else "No failure predicted"
        print(prediction)
        return jsonify({"prediction": float(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)