Here's a professional `README.md` template for your **California House Price Predictor** project:

---

# 🏠 California House Price Predictor

A machine learning web application built with **Streamlit** to predict house prices in California using the California Housing Dataset. This project explores data preprocessing, feature engineering, multiple regression models, hyperparameter tuning, and deployment in an interactive interface.

## 📊 Project Overview

This project used real estate data to predict the **median house value** based on various housing and demographic features. The final model is built using a **Random Forest Regressor**, optimized via Grid Search, and deployed through a user-friendly Streamlit interface.

---

## 🚀 Features

* 🧹 Data preprocessing and feature engineering
* 📈 Exploratory Data Analysis (EDA)
* 🧠 Multiple regression models:

  * Linear Regression
  * Support Vector Regression (SVR)
  * K-Nearest Neighbors (KNN)
  * Random Forest (with hyperparameter tuning)
* 🌐 Web app built with Streamlit
* 🔍 Model interpretability using correlation heatmaps
* 📦 Model saved and loaded using `joblib`

---

## 📂 Dataset

* **Source**: [California Housing Dataset](https://www.kaggle.com/datasets/camnugent/california-housing-prices)
* **Features**:

  * Geographical: `longitude`, `latitude`
  * Housing: `total_rooms`, `total_bedrooms`, `households`, `housing_median_age`
  * Demographic: `population`, `median_income`
  * Categorical: `ocean_proximity`

---

## 🛠️ Tech Stack

* **Python Libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `joblib`, `streamlit`
* **Model**: `RandomForestRegressor` (with GridSearchCV)
* **Deployment**: Streamlit

---

## 📈 Model Training

* Preprocessed features using logarithmic transformations
* One-hot encoded categorical features (`ocean_proximity`)
* Engineered new features:

  * `bedroom_ratio` = total\_bedrooms / total\_rooms
  * `rooms_per_household` = total\_rooms / households
* Split data: 80% training / 20% testing
* Model evaluation metric: **R² score**

---

## 🧪 Model Comparison

| Model                           | R² Score   |
| ------------------------------  | ---------- |
| Linear Regression               |            |
| Random Forest                   |            |
| **Random Forest + GridSearch**  | ✅ **Best**|
| SVR (RBF Kernel)                |            |
| KNN Regressor                   |            |

> ✅ Best performance achieved using **Random Forest with GridSearchCV**.

---

## 🎯 Streamlit App Preview

The app allows users to input:

* Longitude & Latitude
* Housing Median Age
* Total Rooms & Bedrooms
* Population
* Number of Households
* Median Income
* Proximity to Ocean 

### 💡 Output:

Predicted **Median House Value** (in USD).

---

## 🙋‍♂️ Author

**Yi Wang**
- AI Student
- Machine Learning Enthusiast
- 📧 yiwang.ai.tech@gmail.com
