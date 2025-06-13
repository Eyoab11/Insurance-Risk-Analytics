# AlphaCare Insurance: Risk Analytics & Modeling

[![CI Pipeline](https://github.com/<YOUR_USERNAME>/Insurance-Risk-Analytics/actions/workflows/ci_pipeline.yml/badge.svg)](https://github.com/<YOUR_USERNAME>/Insurance-Risk-Analytics/actions)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)

End-to-end analysis of car insurance data to optimize marketing strategies and develop predictive pricing models for AlphaCare Insurance Solutions (ACIS).

## 🎯 Project Goals
1. **Risk Segmentation**: Identify low-risk customer profiles for premium reduction
2. **Marketing Optimization**: Target profitable customer segments
3. **Predictive Modeling**: Build data-driven pricing models

## ⚙️ Quick Start

```bash
# Clone repository
git clone https://github.com/<YOUR_USERNAME>/Insurance-Risk-Analytics.git
cd Insurance-Risk-Analytics

# Install dependencies
pip install -r requirements.txt

# Prepare data
python scripts/convert_to_csv.py

# Launch EDA
jupyter notebook notebooks/task_1_eda.ipynb

## 📊 Phase 1: Exploratory Data Analysis (Complete)

### Key Findings

| Insight Area         | Finding                                                                 | Business Impact                          |
|----------------------|-------------------------------------------------------------------------|------------------------------------------|
| **Geographic Risk**  | Limpopo has 25% higher loss ratio than Western Cape                    | Regional pricing adjustments needed      |
| **Vehicle Risk**     | Luxury vehicles (BMW/Mercedes) show 3x claim severity                  | Vehicle-specific premium tiers           |
| **Temporal Patterns**| December claims spike by 40% vs. annual average                        | Seasonal pricing strategies              |

### Folder Structure
Insurance-Risk-Analytics/
├── data/                   # Raw and processed data
├── notebooks/              # Jupyter notebooks
│   ├── task_1_eda.ipynb    # Completed EDA
│   └── task_2_*.ipynb      # Upcoming analyses
├── scripts/                # Data processing
└── plots/                  # Visualizations