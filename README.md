# Fashion-Brand-Price-Prediction
# 🧵 Fashion Brand Price Prediction – MachineHack Hackathon

This repository contains my solution to the [MachineHack Hackathon](https://machinehack.com/hackathons/predicting_the_price_tag_of_fashion_brands) challenge: **Predicting the Price Tag of Fashion Brands**.

## 📌 Challenge Overview
Participants were tasked with predicting the `Avg_fashion_item_Price` for various fashion brands based on features such as:

- Brand Size
- Sustainable Practices
- Environmental & Labor Indicators
- Customer Engagement Metrics

The goal was to **build a machine learning model** that minimizes the **Root Mean Squared Error (RMSE)**.

## 📁 Dataset
- `Train.csv` — Training data with features and target variable
- `Test.csv` — Test data without target
- `Submission.csv` — Template for final predictions

## 🧠 Approach

1. **Data Preprocessing**
   - Handled missing values
   - Removed irrelevant columns
   - Checked data types and categorical variables

2. **Modeling**
   - Trained multiple regression models (RandomForest, XGBoost, CatBoost)
   - Chose CatBoost for final submission based on lowest RMSE

3. **Hyperparameter Tuning**
   - Tuned key parameters like learning rate, depth, and iterations
   - Used train-test split and cross-validation to ensure generalization

4. **Prediction**
   - Predicted on test data and created final `submission.csv`

## ✅ Libraries Used
- `pandas`
- `numpy`
- `catboost`
- `scikit-learn`

## 📦 Files Included
- `solution.py` – Final training and prediction script
- `final_submission.csv` – Submission file ready for MachineHack
- `README.md` – Project overview

## 🚀 Results
Achieved strong model performance and successfully generated valid predictions for submission. Future improvements can include:
- Feature engineering
- Model ensembling
- Advanced tuning techniques

---

## 🧠 Author
**Adhitya Yellapu**  
Connect on [LinkedIn](https://www.linkedin.com/in/adhitya-yellapu)
