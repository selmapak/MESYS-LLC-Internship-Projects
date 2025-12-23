# Ames House Price Prediction

This project predicts house prices for Ames, Iowa using machine learning models. 
The dataset contains 79 explanatory variables describing almost every aspect of residential homes.

## Project Goals
- Perform EDA (Exploratory Data Analysis) on the Ames dataset.
- Apply feature engineering techniques.
- Train models including Ridge Regression and Gradient Boosting Regressor.
- Evaluate models using RMSE on log-transformed SalePrice.
- Generate predictions for test data and prepare `submission.csv`.

## Analysis & Feature Engineering
- Performed EDA to understand feature distributions and missing values.
- Created 'HasBsmt' to indicate whether a house has a basement and applied log transformations to normalize skewed distributions of numeric features like TotalBsmtSF and SalePrice.
- Converted categorical variables into dummy variables.
- Trained Ridge Regression and Gradient Boosting Regressor models.

## Modeling Results
- Ridge Regression CV RMSE: 0.156
- Gradient Boosting CV RMSE: 0.126
- Gradient Boosting outperformed Ridge Regression, suggesting it captures non-linear relationships in the data more effectively.

## Usage
1. Open `notebooks/Ames_EDA_Modeling.ipynb`.
2. Run all cells to reproduce EDA, feature engineering, and modeling.
3. The final predictions for test data are saved in `submission.csv`.
