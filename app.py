# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import scipy.stats as stat

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
        minTemp = minTemp**(1/1.2)
        # MaxTemp
        maxTemp = float(request.form['Maximum_Temperature'])
        maxTemp = maxTemp**(1/1.2)
        # Rainfall
        rainfall = float(request.form['Rainfall'])
        # Evaporation
        evaporation = float(request.form['Evaporation'])
        evaporation = evaporation**(1/2)
        # Sunshine
        sunshine = float(request.form['Sunshine'])
        sunshine = sunshine**2
        # Wind Gust Speed
        windGustSpeed = float(request.form['Wind_Gust_Speed'])
        windGustSpeed = np.array([windGustSpeed,1])
        windGustSpeed,_=stat.boxcox(windGustSpeed)
        windGustSpeed = windGustSpeed[0]
        # Wind Speed 9am
        windSpeed9am = float(request.form['Wind_Speed_9am'])
        windSpeed9am = windSpeed9am**(1/1.2)
        # Wind Speed 3pm
        windSpeed3pm = float(request.form['Wind_Speed_3pm'])
        windSpeed3pm = windSpeed3pm**(1/1.2)
        # Humidity 9am
        humidity9am = float(request.form['Humidity_9am'])
        humidity9am = humidity9am**(1/1.2)
        # Humidity 3pm
        humidity3pm = float(request.form['Humidity_3pm'])
        humidity3pm = humidity3pm**(1/1.2)
        # Pressure 9am
        pressure9am = float(request.form['Pressure_9am'])
        pressure9am = pressure9am**(1/1.2)
        # Pressure 3pm
        pressure3pm = float(request.form['Pressure_3pm'])
        pressure3pm = np.array([pressure3pm,1])
        pressure3pm,_=stat.boxcox(pressure3pm)
        pressure3pm = pressure3pm[0]
        # Temperature 9am
        temp9am = float(request.form['Temperature_9am'])
        temp9am = temp9am**(1/1.2)
        # Temperature 3pm
        temp3pm = float(request.form['Temperature_3pm'])
        temp3pm = temp3pm**(1/1.2)
        # Cloud 9am
        cloud9am = float(request.form['Cloud_9am'])
        cloud9am = np.where(cloud9am>8,8,cloud9am)
        # Cloud 3pm
        cloud3pm = float(request.form['Cloud_3pm'])
        cloud3pm = np.where(cloud3pm>8,8,cloud3pm)
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
        
        #if my_prediction == 1:
            #result = ' It is a Rainy aday'
        #else:
            #result = ' It is a sunny day'
        #print(result)    
        return render_template('results.html',pred=my_prediction)
    #else:
        #return "error"   

        
if __name__ == '__main__':
    app.run(debug=True)