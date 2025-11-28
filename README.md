# Metro Customer Churn Prediction App

A Streamlit web application to predict customer churn for a metro system using machine learning.

## Overview

This project aims to help metro authorities retain customers by predicting which users are likely to stop using the service. By identifying at-risk customers, targeted interventions can be made.

## Features

- **Interactive Dashboard:** Built with Streamlit for easy interaction.
- **Churn Prediction:** Uses a trained Machine Learning model to predict churn probability.
- **User-Friendly:** Simple input fields for customer data.

## Tech Stack

- **Python:** Core programming language.
- **Streamlit:** Web framework for the user interface.
- **Scikit-learn:** Machine Learning library.
- **Pandas/NumPy:** Data manipulation.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Vallabh409/metro-churn-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd metro-churn-app
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```
The app will open in your default web browser.

## Project Structure

- `app.py`: Main application file.
- `metro_churn_model.pkl`: Pre-trained machine learning model.
- `requirements.txt`: List of Python dependencies.
