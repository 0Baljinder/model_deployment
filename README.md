## Flight Fare Prediction – Render Deployment Web App

This repository contains the code required to deploy the Flight Fare Price Prediction Web App using Render. The deployed site allows users to input flight details (like airline, cities, stops, class, etc.) and receive a predicted flight fare — powered by a machine learning model trained on real airline pricing data.

**webapp link** https://flight-fare-predictor-yie4.onrender.com

**Notice on Prediction Delay**

> Note: This app is hosted on Render's free tier, where the server goes into sleep mode after 15 minutes of inactivity.
When you press the Submit button, the model may take 40–60 seconds to respond if the server is waking up from sleep.
Please be patient — this delay occurs only on the first request after a period of inactivity. Subsequent responses will be much faster.


**Notice**

> This repository focuses only on deployment, while the actual model training, experimentation, and EDA are available in a separate repository : https://github.com/0Baljinder/flight-fare-prediction-using-xgboost-catboost-lgbmboost




---

 ## Purpose of This Repository

Render, a cloud platform for hosting web apps, requires the entire project to be structured in a way it can automatically run app.py or main.py and detect dependencies from files like requirements.txt.

Because of that, we created this dedicated deployment repository, which:

Includes a lightweight version of the full project — just enough to host the trained model

Loads a pre-trained model and pipeline, originally created in another repo

Uses a Flask web framework to interact with users and make predictions



---


## About the Web App

Once deployed using Render, the app allows users to:

Select airline, class, source/destination, times, etc.

Enter values for duration and days left

Get a predicted fare based on the trained ML model


The model used here is based on XGBoost, chosen for its slightly better performance over CatBoost and LightGBM.


---

## How to Deploy This on Render Yourself

If you'd like to try deploying this yourself:

1. Fork or clone this repository


2. Create an account at https://render.com


3. Click "New Web Service" > Connect your GitHub > Select this repo


4. Set the Start Command as:

gunicorn app:app


5. Set the Python Environment and make sure requirements.txt is detected


6. Hit deploy 




---

## Requirements

All required packages are listed in requirements.txt.
Render will install them automatically during deployment.


---

## Main Repository for Full Project (EDA, ML, Training)

This repo only handles deployment.

**The full machine learning project, including model training, data preprocessing, and exploration, is hosted here:**
🔗 Main ML Repository – Flight Fare Price Prediction


---

## Together They Make a Single Project

These two repositories are meant to complement each other:

 ML Repo: Everything related to understanding the data and building the model

 Deployment Repo (this one): Final result as an interactive, hosted app



---

## Screenshots 

You can add one or two screenshots here from the deployed web app.

![Web App Screenshot](screenshots/Screenshot_2025-07-07-10-48-32-188_com.opera.browser.jpg)
![Web App Screenshot](screenshots/Screenshot_2025-07-07-11-03-30-398_com.opera.browser.jpg)
![Web App Screenshot](screenshots/Screenshot_2025-07-07-11-04-10-381_com.opera.browser.jpg)
![Web App Screenshot](screenshots/Screenshot_2025-07-07-10-49-52-966_com.opera.browser.jpg) 
![Web App Screenshot](screenshots/Screenshot_2025-07-07-10-52-34-870_com.opera.browser.jpg)
---


