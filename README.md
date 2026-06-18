# IBM Applied DataScience Capstone Project: SpaceX Falcon 9 First Stage Landing Prediction

## Project Overview

The **Applied Data Science Capstone** is the final project of the **IBM Data Science Professional Certificate**. This project applies the concepts and techniques learned throughout the specialization to solve a real-world data science problem.

SpaceX has transformed the commercial space industry by reducing launch costs through the reuse of Falcon 9 rocket first stages. A Falcon 9 launch costs approximately **$62 million**, while other providers may charge over **$165 million**. The major cost advantage comes from the ability to recover and reuse the first stage.

The goal of this project is to use publicly available data and machine learning techniques to predict whether the Falcon 9 first stage will successfully land. This prediction can help estimate launch costs and identify the factors that influence landing success.

---

## 🎯 Project Objectives

This project focuses on answering the following questions:

- How do variables such as **payload mass, launch site, flight number, and orbit type** affect the success of Falcon 9 first-stage landings?
- Does the success rate of first-stage landings increase over the years?
- Which **machine learning classification algorithm** performs best for predicting landing success?

---

## 🛠️ Methodology

### 1. Data Collection

Data was collected using the following sources:

- **SpaceX REST API** to obtain launch data.
- **Web scraping from Wikipedia** to gather additional historical launch information.

---

### 2. Data Wrangling and Preprocessing

The collected data was prepared through:

- Filtering and selecting relevant data.
- Handling missing values.
- Performing data transformation and feature engineering.
- Applying **One-Hot Encoding** to convert categorical variables into numerical features for machine learning models.

---

### 3. Exploratory Data Analysis (EDA)

Exploratory analysis was performed using:

- Data visualization techniques to identify patterns and trends.
- SQL queries for deeper data exploration.
- Analysis of relationships between launch characteristics and landing success.

---

### 4. Interactive Visual Analytics

Interactive dashboards and visualizations were created using:

- **Folium** for geographical analysis of launch sites.
- **Plotly Dash** for interactive exploration of SpaceX launch data.

---

### 5. Predictive Analysis

Multiple classification algorithms were developed and evaluated to predict first-stage landing success:

- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree Classifier
- K-Nearest Neighbors (KNN)

The models were improved using:

- Hyperparameter tuning.
- Performance evaluation.
- Comparison of classification accuracy to identify the best-performing model.

---

## 📌 Project Outcome

This project demonstrates an end-to-end data science workflow, including:

- Data collection and preprocessing
- Exploratory data analysis
- Data visualization
- Interactive dashboard development
- Machine learning model building and evaluation

The final model predicts Falcon 9 first-stage landing success and provides insights into the factors that contribute to successful rocket recovery.
