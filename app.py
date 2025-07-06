
from xgboost import XGBRegressor
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from flask import Flask, request, render_template

import joblib
from sklearn.compose import ColumnTransformer
import pathlib

pipeline=joblib.load('flight_fare_price_pipeline.pkl')

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        data=pd.DataFrame([{'airline':request.form['airline'], 'source_city':request.form['source_city'], 'departure_time': request.form['departure_time'], 'stops': request.form['stops'], 'arrival_time': request.form['arrival_time'], 'destination_city': request.form['destination_city'], 'class': request.form['class'], 'duration': float(request.form['duration']), 'days_left': int(request.form['days_left'])}])
        pred=pipeline.predict(data)
        prediction=np.exp(pred)
        return render_template('result.html', prediction=prediction)
    return render_template('index.html')

