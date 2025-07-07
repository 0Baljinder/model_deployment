## Flight Fare Prediction – Render Deployment Web App

This repository contains the code required to deploy the Flight Fare Price Prediction Web App using Render. The deployed site allows users to input flight details (like airline, cities, stops, class, etc.) and receive a predicted flight fare — powered by a machine learning model trained on real airline pricing data.

> Note: This repository focuses only on deployment, while the actual model training, experimentation, and EDA are available in a separate repository (linked below).




---

 ## Purpose of This Repository

Render, a cloud platform for hosting web apps, requires the entire project to be structured in a way it can automatically run app.py or main.py and detect dependencies from files like requirements.txt.

Because of that, we created this dedicated deployment repository, which:

Includes a lightweight version of the full project — just enough to host the trained model

Loads a pre-trained model and pipeline, originally created in another repo

Uses a Flask web framework to interact with users and make predictions



---

## Key Differences from the Original (Training) Repository

Aspect	Training Repository	Render Deployment Repository

Purpose	Model training, EDA, testing, and validation	Hosting the trained model as a web app
Platform	Google Colab Notebooks, Ngrok for testing	Render (cloud deployment)
Contents	Full ML workflow + notebook	Flask app, model file, app.py, templates
Model Format	Saved via joblib in pipeline form	Loaded and used directly in Flask backend



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

![Web App Screenshot](screenshots/homepage.jpg)


---


