from pickle import load
from flask import Flask, request, jsonify

with open('dv.bin', 'rb') as dv_file:
    dv = load(dv_file)

with open('model2.bin', 'rb') as model_file:
    model = load(model_file)

app = Flask('client-prediction')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    X_client = dv.transform([client])
    probabilities = model.predict_proba(X_client)
    probability = probabilities[0][1]

    return jsonify({'subscription_probability': probability})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9696)
