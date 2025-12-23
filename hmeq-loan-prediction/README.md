This project focuses on predicting credit risk using the **HMEQ (Home Equity)** dataset. The goal is to identify high-risk loan applicants to minimize financial losses for banking institutions.

##  Project Highlights
* **Problem Type:** Binary Classification (Default vs. Non-Default)
* **Key Tools:** Python, Scikit-learn, Pandas, Joblib
* **Winning Model:** Random Forest (Optimized via GridSearchCV)
* **Main Metric:** F1-Score (Due to imbalanced classes)

##  Workflow
1. **Data Cleaning:** Handled missing values using median/mode imputation.
2. **Feature Engineering:** One-Hot Encoding for categorical variables like `JOB` and `REASON`.
3. **Scaling:** Applied `StandardScaler` for robust model performance.
4. **Insights:** Identified `DEBTINC` (Debt-to-Income) as the most critical risk factor.

##  Deployment Ready
The trained model and scaler are exported as `.joblib` files, making it ready for production API integration.
