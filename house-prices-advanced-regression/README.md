# House Price Prediction (Ames Housing)

An end-to-end Machine Learning project to predict house prices in Ames, Iowa. This project demonstrates advanced data transformation and regression techniques.

## Project Highlights
* **Problem Type:** Regression (Predicting SalePrice)
* **Key Tools:** Python, Seaborn, Scikit-learn, NumPy
* **Core Technique:** Log Transformation & Feature Engineering
* **Best Model:** Random Forest Regressor

## Technical Steps
1. **EDA:** Identified correlations between house quality (`OverallQual`) and price.
2. **Outlier Removal:** Cleaned extreme values in `GrLivArea` to stabilize the model.
3. **Feature Engineering:** Created a custom `TotalSF` (Total Square Footage) feature.
4. **Target Transformation:** Applied `log1p` to handle skewness in target variable.

## Results
The model achieves a high accuracy with minimized **RMSE** (Root Mean Squared Error). A `submission.csv` was generated for evaluation.
