from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route('https://mark-prediction.onrender.com/predict', methods=['POST'])
def predict():
    data = request.get_json()
    hours = float(data['hours'])

    prediction = model.predict([[hours]])

    return jsonify({
        "predicted_marks": float(prediction[0])
    })

if __name__ == '__main__':
    app.run(debug=True)