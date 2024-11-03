# Telme

Welcome to **Telme**, a smart solution that uses **machine learning models (K-means and Logistic Regression)** to assign users to clusters and recommend the best plan based on their input. This project demonstrates a seamless **telecommunication plan recommendation engine** built with **Python and Scikit-learn**.

---

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Language Used](#language-used)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How it Works](#how-it-works)

---

## Features
- **User Input Handling**: Collects user details including city, days since joining, and number of plan changes.
- **K-means Clustering**: Assigns the user to an appropriate cluster based on input.
- **Logistic Regression**: Recommends the ideal plan for the user.

---

## Tech Stack
- **Backend**: Python, Scikit-learn
- **Machine Learning Models**: K-means, Logistic Regression
- **Data Handling**: Pandas, Numpy
- **Deployment**: Local development with Flask

---

## Language Used
- Python


## Usage
- Open the Web Interface: Enter your city, days since joining, and total plan changes.
- Submit the Form: The app assigns you to a cluster and recommends the ideal plan based on your input.
- View Recommendation: See the recommended plan displayed in the web interface.


## Project Structure
   ```perl
   plan-recommendation-system/
   │
   ├── templates/
   │   └── index.html               # Frontend HTML
   ├── .venv/                       # Virtual environment (ignored in Git)
   ├── app.py                       # Flask backend
   ├── FinalScript.py               # Main ML logic
   ├── requirements.txt             # Python dependencies
   ├── models/                      # Serialized ML models and encoders
   │   ├── kmeans_model.pkl
   │   ├── logistic_model.pkl
   │   ├── city_encoder.pkl
   │   ├── plan_encoder.pkl
   │   └── scaler.pkl
   └── README.md                    # Project documentation
```

## How it Works
- User Input: The user provides details such as city, days since joining, total plan changes, and selected plans.
- K-means Clustering: The user is assigned to one of three clusters.
- Logistic Regression: Based on the cluster and city, a recommended plan is generated.
- Plan Recommendation: The recommended plan is displayed on the frontend

