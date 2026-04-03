from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)   # 🔥 IMPORTANT LINE

model = pickle.load(open("model.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    hours = float(data['hours'])   # convert to float

    prediction = model.predict([[hours]])

    return jsonify({
        'predicted_marks': float(prediction[0])
    })

if __name__ == '__main__':
    app.run(debug=True)