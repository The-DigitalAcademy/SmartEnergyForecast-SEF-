import joblib as jb
from joblib import dump, load
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import r2_score
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Specify the file path and column names to read
file_path = "/Users/da_learner_m1_19/Downloads/SmartEnergyForecast-SEF--5/Python/myupdateddata.csv"
columns_to_read = ["Residual Demand", "RSA Contracted Demand", "Thermal Generation", "Pumped Water Generation", "Pumped Water SCO Pumping"]


# Read the CSV file and select only the specified columns
data = pd.read_csv(file_path, usecols=columns_to_read)

# Split the data into a features DataFrame and a target variable Series
features = data.drop('Residual Demand', axis=1)
target = data['Residual Demand']

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.1, random_state=42)

# Train a linear regression model using only the selected columns
model = LinearRegression()
model.fit(X_train, y_train)

# Calculate the mean squared error (MSE) of the model on the test set
y_pred_test = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred_test)
r2_test=r2_score(y_test,y_pred_test)

# save the model to a file
jb.dump(model, 'linear_regression_model.joblib')

# load the model from the file
loaded_model = load('linear_regression_model.joblib')
from sklearn.metrics import r2_score

filename = 'linear_regression_model.joblib'
jb.dump(model,filename)
print('Linear regression model saved successfully to', filename)
r2=r2_score(y_test,y_pred_test)
