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