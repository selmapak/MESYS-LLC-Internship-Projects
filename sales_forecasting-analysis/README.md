#  Order Demand Forecasting with SARIMAX

This project focuses on forecasting daily food order demand for an online delivery company using **time series analysis**.  
The forecasts are designed to support **operational planning**, such as determining the required number of couriers, motorcycles, and workforce allocation.

The model incorporates **external (exogenous) variables** such as **temperature** and **advertising spend**, which are known to influence customer ordering behavior.

---

##  Dataset Description

- **Date Range:** 2 May 2020 – 30 June 2022  
- **Frequency:** Daily

### Variables

| Column Name   | Description |
|--------------|------------|
| `date`        | Daily date |
| `orders`     | Number of orders per day (target variable) |
| `temperature`| Daily average temperature |
| `media_spend`   | Daily advertising expenditure |

Key assumptions:
- Orders tend to **increase during colder weather** as customers prefer staying at home.
- Higher **advertising spend** generally leads to an increase in orders.

---

##  Project Objectives

- Perform **exploratory data analysis (EDA)** and visualize trends and seasonality.
- Handle **missing values** and **outliers** appropriately.
- Build baseline and advanced **time series models**.
- Incorporate **exogenous variables** using SARIMAX.
- Optimize model parameters using **time series cross-validation**.
- Evaluate performance using a **time-based train-test split**.
- Generate **future demand forecasts** for operational decision-making.
- Save the trained model for **production or API usage**.

---

##  Methodology

### 1. Data Preprocessing
- Missing values handled using **forward fill**, suitable for time series data.
- Outliers in order counts treated using the **Interquartile Range (IQR)** method.
- Data sorted chronologically to preserve temporal structure.

### 2. Exploratory Data Analysis
- Visualization of order trends over time.
- Analysis of relationships between orders and:
  - Temperature
  - Advertising spend
- Inspection of seasonality and potential trend components.

### 3. Train–Test Split
- Data split based on time (not randomly).
- Last **20%** of observations used as the test set to avoid data leakage.

### 4. Modeling Approach
- **SARIMAX (Seasonal ARIMA with Exogenous Variables)** selected to:
  - Capture trend and seasonality.
  - Incorporate temperature and advertising spend as external regressors.
- Model parameters optimized using **TimeSeriesSplit cross-validation**.

### 5. Evaluation Metrics
- Root Mean Squared Error (**RMSE**)
- Mean Absolute Error (**MAE**)

Both training and test performance are analyzed to detect potential overfitting.

---

##  Forecasting Strategy

- After evaluating test performance, the model is **retrained on the full dataset**.
- A **30-day forecast horizon** is defined.
- Forecasts start from the day **after the last observed date** (1 July 2022).
- Future values of temperature and advertising spend are provided as inputs.
- Forecasting is performed using `get_forecast()` to ensure correct handling of exogenous variables.

---

##  Visualizations

The project includes:
- Historical order trends
- Orders vs temperature scatter plots
- Orders vs advertising spend scatter plots
- Train–test split visualization
- Actual vs predicted values for train and test sets
- Historical data combined with future forecasts

These visualizations provide transparency and help validate model behavior from both technical and business perspectives.

---

## Model Persistence

The final SARIMAX model is saved using `joblib`:

```python
joblib.dump(final_model, "order_forecast_sarimax.pkl")
