from flask import Flask,render_template,url_for,request
from sklearn.externals import joblib
import numpy as np
import pandas as pd

app=Flask(__name__)

rain_model =joblib.load('rain_model.pkl')
temp_model=joblib.load('temp_model.pkl')

@app.route('/',methods=['GET','POST'])
def hello():
    if request.method=='GET':
        return render_template('home.html')
    elif request.method=='POST':
        dewptm1 = int(request.form['dewptm1'])
        fog1 = int(request.form['fog1'])
        hail1 = int(request.form['hail1'])
        hum1 = int(request.form['hum1'])
        pressure1 = int(request.form['pressure1'])
        rain1 = int(request.form['rain1'])
        snow1 = int(request.form['snow1'])
        temp1 = int(request.form['temp1'])
        tornado1 = int(request.form['tornado1'])
        wdird1= int(request.form['wdird1'])
        # DAY 2 DATA BELOW   
        dewptm2 = int(request.form['dewptm2'])
        fog2 = int(request.form['fog2'])
        hail2 = int(request.form['hail2'])
        hum2 = int(request.form['hum2'])
        pressure2 = int(request.form['pressure2'])
        rain2 = int(request.form['rain2'])
        snow2 = int(request.form['snow2'])
        temp2 = int(request.form['temp2'])
        tornado2 = int(request.form['tornado2'])
        wdird2 = int(request.form['wdird2'])
        # DAY 3 DATA BELOW
        dewptm3 = int(request.form['dewptm3'])
        fog3 = int(request.form['fog3'])
        hail3 = int(request.form['hail3'])
        hum3 = int(request.form['hum3'])
        pressure3 = int(request.form['pressure3'])
        rain3 = int(request.form['rain3'])
        snow3 = int(request.form['snow3'])
        temp3 = int(request.form['temp3'])
        tornado3 = int(request.form['tornado3'])
        wdird3 = int(request.form['wdird3'])
        temp_prediction=temp_model.predict(np.array([[dewptm1,fog1,hail1,hum1,pressure1,rain1,snow1,temp1,tornado1,wdird1,dewptm2,fog2,hail2,hum2,pressure2,rain2,snow2,temp2,tornado2,wdird2,dewptm3,fog3,hail3,hum3,pressure3,rain3,snow3,temp3,tornado3,wdird3]]))
        rain_prediction=rain_model.predict(np.array([[dewptm1,fog1,hail1,hum1,pressure1,rain1,snow1,temp1,tornado1,wdird1,dewptm2,fog2,hail2,hum2,pressure2,rain2,snow2,temp2,tornado2,wdird2,dewptm3,fog3,hail3,hum3,pressure3,rain3,snow3,temp3,tornado3,wdird3]]))
        temp=str(temp_prediction).strip('[]')
        rain=str(rain_prediction).strip('[]')
        if rain=='0':
            rain_new='Our predicted value is ' + rain + ' . Hence, Chance of Rain are less than 50% '
        else:
            rain_new='Our predicted value is ' + rain + ' . Hence, High Probability of rain tomorrow'    
        if (int(temp_prediction)<25) and (int(rain_prediction)==1) :
            comments="It is going to be a pleasant day tomorrow and there is high probability for rain"
        elif (int(temp_prediction) < 25) and (int(rain_prediction) == 0):
            comments="It is going to be a pleasant day tomorrow ,however there are less chance for rain"
        elif (int(temp_prediction) > 25) and (int(rain_prediction) == 0):
            comments="It is going to be hot tomorrow"
        elif (int(temp_prediction) > 25) and (int(rain_prediction) == 1):
            comments="It is going to be hot but there are chance of shower tomorrow"
        return render_template('predicted.html',temp=temp,rain=rain_new,comments=comments)

        
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
