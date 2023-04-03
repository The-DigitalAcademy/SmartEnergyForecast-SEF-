import flask
import joblib
import pandas as pd

app = flask.Flask(__name__)

# Load the model
model = joblib.load("linear_regression_model.joblib")

@app.route('/', methods=['GET', 'POST'])
def predict():
    if flask.request.method == 'POST':
        # Get the input data from the user
        input_data = flask.request.form['input_data']
        
        # Preprocess the input data
       if flask.request.method == 'POST':
    # Get the input data from the user
        input_data = {
            'DateTimeHourBeginning': [flask.request.form['DateTimeHourBeginning']],
            'ResidualForecast': [float(flask.request.form['ResidualForecast'])],
            'RSAContractedForecast': [float(flask.request.form['RSAContractedForecast'])],
            'DispatchableGeneration': [float(flask.request.form['DispatchableGeneration'])],
            'ResidualDemand': [float(flask.request.form['ResidualDemand'])],
            'RSAContractedDemand': [float(flask.request.form['RSAContractedDemand'])],
            'InternationalExports': [float(flask.request.form['InternationalExports'])],
            'InternationalImports': [float(flask.request.form['InternationalImports'])],
            'ThermalGeneration': [float(flask.request.form['ThermalGeneration'])],
            'NuclearGeneration': [float(flask.request.form['NuclearGeneration'])],
            'EskomGasGeneration': [float(flask.request.form['EskomGasGeneration'])],
            'EskomOCGTGeneration': [float(flask.request.form['EskomOCGTGeneration'])],
            'HydroWaterGeneration': [float(flask.request.form['HydroWaterGeneration'])],
            'PumpedWaterGeneration': [float(flask.request.form['PumpedWaterGeneration'])],
            'ILSUsage': [float(flask.request.form['ILSUsage'])],
            'ManualLoadReductionMLR': [float(flask.request.form['ManualLoadReductionMLR'])],
            'IOSExclILSandMLR': [float(flask.request.form['IOSExclILSandMLR'])],
            'DispatchableIPPOCGT': [float(flask.request.form['DispatchableIPPOCGT'])],
            'EskomGasSCO': [float(flask.request.form['EskomGasSCO'])],
            'EskomOCGTSCO': [float(flask.request.form['EskomOCGTSCO'])],
            'HydroWaterSCO': [float(flask.request.form['HydroWaterSCO'])],
            'PumpedWaterSCOPumping': [float(flask.request.form['PumpedWaterSCOPumping'])],
            'Wind': [float(flask.request.form['Wind'])],
            'PV': [float(flask.request.form['PV'])],
            'CSP': [float(flask.request.form['CSP'])],
            'OtherRE': [float(flask.request.form['OtherRE'])],
            'TotalRE': [float(flask.request.form['TotalRE'])],
            'WindInstalledCapacity': [float(flask.request.form['WindInstalledCapacity'])],
            'PVInstalledCapacity': [float(flask.request.form['PVInstalledCapacity'])],
            'CSPInstalledCapacity': [float(flask.request.form['CSPInstalledCapacity'])],
            'OtherREInstalledCapacity': [float(flask.request.form['OtherREInstalledCapacity'])],
            'TotalREInstalledCapacity': [float(flask.request.form['TotalREInstalledCapacity'])],
            'InstalledEskomCapacity': [float(flask.request.form['InstalledEskomCapacity'])],
            'TotalPCLF': [float(flask.request.form['TotalPCLF'])],
            'TotalUCLF': [float(flask.request.form['TotalUCLF'])],
            'TotalOCLF': [float(flask.request.form['TotalOCLF'])],
            'TotalUCLFOCLF': [float(flask.request.form['TotalUCLFOCLF'])]
            




        # Make predictions using the model
        predictions = model.predict(input_data)
        
        # Return the predictions as a response to the user
        return flask.render_template('index.html', predictions=predictions[0])
    
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

