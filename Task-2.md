# Interim Report: Insurance Risk Analytics  

**Author**: [Your Name]  
**Date**: June 13, 2025  
**Repository**: [GitHub Repository Link]  

---

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