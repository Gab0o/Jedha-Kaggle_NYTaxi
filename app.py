from flask import Flask, request
from joblib import load
import json


app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    values = json.loads(request.form['values'])
    model = load('taxi_model')
    prediction = model.predict(values)
    return json.dumps(prediction.tolist())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)