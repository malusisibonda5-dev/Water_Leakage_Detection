\# 💧 Water Leakage Detection System



&#x20;Project Overview



The Water Leakage Detection System is a machine learning application designed to predict whether a water pipe is likely to experience leakage based on sensor and operational information.



The system uses a Logistic Regression classification model and provides predictions through an interactive Streamlit application.



\## Problem Statement



Undetected water leaks can result in water wastage, increased maintenance costs and damage to water infrastructure.



This project uses machine learning to identify patterns in pipe sensor data that can help predict potential water leakage.



&#x20;Dataset



The dataset contains 5,000 records and includes sensor, operational and location-related information.



\### Features



\- Pressure

\- Flow Rate

\- Temperature

\- Vibration

\- RPM

\- Operational Hours

\- Zone

\- Block

\- Pipe



\### Target Variable



\- Leakage\_Flag

&#x20; - 0 = No Leakage

&#x20; - 1 = Leakage



\## Machine Learning Process



The project follows the machine learning lifecycle:



1\. Data loading

2\. Data cleaning

3\. Exploratory Data Analysis

4\. Feature engineering

5\. Data preprocessing

6\. Train-test splitting

7\. Model training

8\. Prediction

9\. Model evaluation

10\. Model saving

11\. Application deployment



\## Model



The final application uses \*\*Logistic Regression\*\* for binary classification.



The model predicts:



\- No Water Leakage

\- Water Leakage



The application also displays the probability associated with the prediction.



\## Model Evaluation



The model was evaluated using:



\- Accuracy

\- Precision

\- Recall

\- F1-Score

\- Confusion Matrix



The final Logistic Regression model achieved:



\- Accuracy: 96.19%

\- Precision: 81.63%

\- Recall: 58.82%

\- F1-Score: 68.38%



\## Application



The Streamlit application allows a user to enter pipe sensor information and receive a water leakage prediction.



The application displays:



\- Prediction result

\- Leakage probability

\- No-leakage probability



&#x20;Project Files





Water\_Leakage\_Detections

│

├── app.py

├── final\_model.pkl

├── scaler.pkl

├── requirements.txt

├── Leakeage\_Prediction.ipynb

└── README.md

