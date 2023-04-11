from flask import Flask, request, render_template
import joblib as jb
from joblib import load
import numpy as np

app = Flask(__name__)

model = jb.load('linear_regression_model.joblib')

loaded_model = load('linear_regression_model.joblib')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # ResidualDemand = float(request.form['ResidualDemand'])
        RSAContractedDemand = float(request.form['RSAContractedDemand'])
        ThermalGeneration = float(request.form['ThermalGeneration'])
        PumpedWaterGeneration = float(request.form['PumpedWaterGeneration'])
        PumpedWaterSCOPumping = float(request.form['PumpedWaterSCOPumping'])

        data = np.array([RSAContractedDemand, ThermalGeneration, PumpedWaterGeneration, PumpedWaterSCOPumping]).reshape(1, -1)

        prediction = loaded_model.predict(data)[0]
        
        return render_template('index.html', prediction=prediction)

    data = [
        request.form['ResidualDemand'],
        request.form['RSAContractedDemand'],
        request.form['ThermalGeneration'],
        request.form['PumpedWaterGeneration'],
        request.form['PumpedWaterSCOPumping']
    ]

    predict = model.predict(data)  

    return render_template('index.html', prediction=predict[0])


if __name__ == '__main__':
    app.run(debug=True, port=5001)
