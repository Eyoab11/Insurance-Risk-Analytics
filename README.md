## Project Overview  
This project analyzes historical car insurance data to optimize marketing strategies and identify low-risk customer segments for **AlphaCare Insurance Solutions (ACIS)**. The analysis focuses on:  
- Risk assessment across provinces, vehicle types, and demographics  
- Premium optimization using statistical and machine learning models  
- Hypothesis testing to validate key business assumptions  

---

## Task 1: Exploratory Data Analysis (EDA)  

### 1. Implementation Summary  
**Data Loading & Cleaning:**  
- Loaded `insurance_data.csv` (pipe-delimited `.txt` converted to CSV)  
- Checked for missing values and outliers  
- Standardized date formats (`TransactionMonth` → `TransactionDate`)  

**Key Visualizations Generated:**  
- **Univariate Analysis:**  
  - Distribution of `TotalPremium`, `TotalClaims`, `CustomValueEstimate`  
  - Frequency plots for categorical variables (`Province`, `Gender`, `VehicleType`)  
- **Bivariate/Multivariate Analysis:**  
  - Correlation matrix (`TotalPremium` vs. `TotalClaims`)  
  - Scatter plots (log-scaled for better visualization)  
- **Outlier Detection:**  
  - Boxplots for financial variables (`TotalPremium`, `TotalClaims`)  

**Key Insight Visualizations:**  
1. **Loss Ratio by Province** → Limpopo shows the highest risk  
2. **Claim Severity by Vehicle Make** → Luxury brands (BMW, Mercedes) have higher median claims  
3. **Monthly Trends** → Premiums grow steadily, but claims are volatile  

### 2. Key Metrics  

| Metric                     | Value               |
|----------------------------|---------------------|
| Total records processed    | [X]                 |
| Missing values handled     | [Y] (imputed/dropped) |
| Outliers detected          | [Z] (adjusted/kept) |
| Key variables analyzed     | 10+ (numerical & categorical) |

### 3. Outputs  
- **Processed Data:** `data/insurance_data.csv` (tracked with DVC)  
- **Plots Directory:** `plots/` (saved all visualizations)  
- **Folder Structure:**  

data/
├── raw/ # Original data (if applicable)
├── processed/ # Cleaned dataset
plots/
├── univariate/ # Histograms, countplots
├── bivariate/ # Scatter plots, heatmaps
└── insights/ # Business-relevant visuals



### 4. Challenges & Solutions  

| Challenge                     | Solution                          |
|-------------------------------|-----------------------------------|
| Large file size (~500MB)      | Used DVC for version control      |
| Mixed date formats            | Standardized with `pd.to_datetime()` |
| Log-scale visualization needed| Applied `plt.xscale('log')`       |

### 5. Next Steps  
1. **Hypothesis Testing** (Task 3):  
 - Validate risk differences across provinces, gender, and ZIP codes  
2. **Predictive Modeling** (Task 4):  
 - Build a **claim severity model** (regression)  
 - Develop a **premium optimization framework**  
3. **DVC Pipeline Enhancement**:  
 - Add more dataset versions (sampled/filtered)  

### 6. Tools Used  
- **Python 3.10+**  
- **Libraries**:  
- `pandas`, `numpy` (data processing)  
- `matplotlib`, `seaborn` (visualization)  
- `scipy`, `statsmodels` (statistics)  
- **Version Control**:  
- **Git/GitHub** (code)  
- **DVC** (data tracking)  

---

## Task 2: Data Version Control (DVC) Setup  

### 1. Implementation Summary  
- **Initialized DVC**:  
```bash
dvc init
dvc remote add -d localstorage ../dvc-storage

# DVC Workflow Summary

## Tracked Data
To track the dataset using DVC and Git:

```bash
dvc add data/insurance_data.csv
git add data/insurance_data.csv.dvc
git commit -m "feat: Track dataset with DVC"
dvc push

## Reproducible Workflow

- Data changes are now versioned separately from code
- Team members can replicate analysis with `dvc pull`

## Key Commands

| Action               | Command               |
|----------------------|-----------------------|
| Track new data       | `dvc add data/file.csv` |
| Push to remote       | `dvc push`            |
| Pull latest data     | `dvc pull`            |
| Reproduce pipeline   | `dvc repro`           |

## Next Steps for DVC

- Add more dataset versions (e.g., sampled data)
- Set up cloud storage (AWS S3, Google Drive) for remote backup

## Conclusion

- **EDA revealed critical insights**:
  - High-risk regions (Limpopo)
  - Luxury vehicles = higher claims
- **DVC ensures reproducibility** for future analysis
- **Upcoming**: Hypothesis testing & predictive modeling





# Task 4: Predictive Modeling for Claim Severity

### **Objective**

The goal of this task was to build and evaluate machine learning models to predict the total claim amount (`TotalClaims`) for policies that have experienced a claim. The insights from the best-performing model will be used to understand key risk drivers and inform pricing strategy.

### **Methodology**

The modeling process followed these key steps:

1.  **Data Preparation:** Loaded the pre-processed `modeling_data.csv` file. The dataset was then filtered to include only policies with claims (`TotalClaims > 0`), resulting in a modeling set of 2,788 records.
2.  **Train-Test Split:** The data was split into an 80% training set and a 20% testing set to ensure a robust evaluation on unseen data.
3.  **Model Training:** Three different regression models were trained:
    *   Linear Regression
    *   Random Forest Regressor
    *   XGBoost Regressor
4.  **Model Evaluation:** Models were evaluated based on two metrics:
    *   **Root Mean Squared Error (RMSE):** The average prediction error in ZAR. Lower is better.
    *   **R-squared (R²):** The proportion of variance in the target variable explained by the model. Higher is better.
5.  **Model Interpretability:** The SHAP (SHapley Additive exPlanations) library was used to analyze the feature importance and impact of the best-performing model.

### **Model Performance Results**

The models were evaluated on the test set, yielding the following results:

| Model               | RMSE (ZAR)   | R-squared |
| ------------------- | ------------ | --------- |
| **Linear Regression** | **34,201.98**| **0.2726**  |
| Random Forest       | 34,747.77    | 0.2492    |
| XGBoost             | 38,991.24    | 0.0547    |

**Conclusion:** Contrary to common expectations, the **Linear Regression** model was the best performer in this iteration, with the lowest error and highest explanatory power.

### **Feature Importance & Interpretation**

SHAP analysis was performed to understand the model's predictions.

![SHAP Bar Plot](./plots/shap_summary_bar.png)

#### **Critical Finding: Data Leakage**

The analysis revealed that the top 3 most influential features are all related to the premium and insured sum:
1.  `CalculatedPremiumPerTerm`
2.  `TotalPremium`
3.  `SumInsured`

This indicates a significant **data leakage** problem. The model is primarily using information about the premium (which is itself calculated based on risk) to predict the claim amount. While this leads to a statistically "correct" model, it is not practically useful for setting premiums for new clients, as it doesn't rely on inherent risk factors.

### **Conclusion & Next Steps**

1.  **Best Performing Model:** In this initial run, Linear Regression performed the best.
2.  **Actionable Insight:** The modeling process has uncovered a critical data leakage issue. The current model's reliance on premium-related features makes it unsuitable for a real-world pricing engine.
3.  **Recommendation for Next Iteration:** The modeling process must be repeated after **removing the leaky features** (`CalculatedPremiumPerTerm`, `TotalPremium`, `SumInsured`) from the feature set. This will force the model to learn from genuine risk drivers like `VehicleAge` and `kilowatts`, providing more valuable and actionable insights for ACIS.