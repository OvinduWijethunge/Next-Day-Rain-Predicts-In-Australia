# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

# Load the Random Forest CLassifier model
filename = 'model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/predict', methods=['GET','POST'])
def predict():
    
    print('hello')
    if request.method == 'POST':
        # DATE
        date = request.form['Date']
        day = float(pd.to_datetime(date, format="%Y-%m-%dT").day)
        month = float(pd.to_datetime(date, format="%Y-%m-%dT").month)
        # MinTemp
        minTemp = float(request.form['Minimum_temprature'])
        # MaxTemp
        maxTemp = float(request.form['Maximum_Temperature'])
        # Rainfall
        rainfall = float(request.form['Rainfall'])
        # Evaporation
        evaporation = float(request.form['Evaporation'])
        # Sunshine
        sunshine = float(request.form['Sunshine'])
        # Wind Gust Speed
        windGustSpeed = float(request.form['Wind_Gust_Speed'])
        # Wind Speed 9am
        windSpeed9am = float(request.form['Wind_Speed_9am'])
        # Wind Speed 3pm
        windSpeed3pm = float(request.form['Wind_Speed_3pm'])
        # Humidity 9am
        humidity9am = float(request.form['Humidity_9am'])
        # Humidity 3pm
        humidity3pm = float(request.form['Humidity_3pm'])
        # Pressure 9am
        pressure9am = float(request.form['Pressure_9am'])
        # Pressure 3pm
        pressure3pm = float(request.form['Pressure_3pm'])
        # Temperature 9am
        temp9am = float(request.form['Temperature_9am'])
        # Temperature 3pm
        temp3pm = float(request.form['Temperature_3pm'])
        # Cloud 9am
        cloud9am = float(request.form['Cloud_9am'])
        # Cloud 3pm
        cloud3pm = float(request.form['Cloud_3pm'])
        # Cloud 3pm
        location = float(request.form['Location'])
        # Wind Dir 9am
        winddDir9am = float(request.form['Wind_Direction_9am'])
        # Wind Dir 3pm
        winddDir3pm = float(request.form['Wind_Direction_3pm'])
        # Wind Gust Dir
        windGustDir = float(request.form['Wind_Gust_Direction'])
        # Rain Today
        rainToday = float(request.form['Rain_Today'])
        
        #data modification 
        

        

        data = np.array([[location,minTemp,maxTemp,rainfall,evaporation,sunshine,windGustDir,windGustSpeed,winddDir9am,winddDir3pm,windSpeed9am,windSpeed3pm,humidity9am,humidity3pm,pressure9am,pressure3pm,cloud9am,cloud3pm,temp9am,temp3pm,rainToday,month,day]])
        my_prediction = classifier.predict(data)
        print(my_prediction)
        result = ''
        if my_prediction == 1:
            result = ' It is a Rainy aday'
        else:
            result = ' It is a sunny day'
        print(result)    
        return render_template('index.html', prediction=result)
        
if __name__ == '__main__':
    app.run(debug=True)