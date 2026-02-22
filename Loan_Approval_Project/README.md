
# 🏦 Loan Approval Prediction

A machine learning project that predicts whether a loan application will be **approved or rejected** based on applicant financial and personal information.

---

## 📌 Project Overview

Financial institutions receive thousands of loan applications daily. Manual evaluation is time-consuming and prone to inconsistency. This project builds a classification model that automates loan approval decisions by learning patterns from historical applicant data — helping lenders make faster, data-driven, and fair credit decisions.

---

## 📊 Dataset

The dataset contains information about loan applicants including:

| Feature | Description |
|---|---|
| `Gender` | Male / Female |
| `Married` | Marital status |
| `Dependents` | Number of dependents |
| `Education` | Graduate / Not Graduate |
| `Self_Employed` | Self-employed or not |
| `ApplicantIncome` | Monthly income of the applicant |
| `CoapplicantIncome` | Monthly income of the co-applicant |
| `LoanAmount` | Loan amount (in thousands) |
| `Loan_Amount_Term` | Term of the loan (in months) |
| `Credit_History` | Credit history meets guidelines (1 = Yes, 0 = No) |
| `Property_Area` | Urban / Semi-Urban / Rural |
| `Loan_Status` | **Target** — Y (Approved) / N (Rejected) |

You can download a similar **Loan Approval Prediction Dataset** from Kaggle:

🔗 **Kaggle Dataset:**  
https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset :contentReference[oaicite:0]{index=0}

This dataset includes relevant features such as credit score, income details, loan amount and the target label `"Loan_Status"`.

---

## 🔍 Workflow

### 1. Exploratory Data Analysis (EDA)
- Distribution of loan approvals across categories
- Correlation between income, loan amount, and approval status
- Handling missing values and outliers
- Visualizations using Matplotlib & Seaborn

### 2. Data Preprocessing
- Imputation of missing values (median for numerical, mode for categorical)
- Label encoding for categorical features
- Feature scaling (StandardScaler)
- Train-test split

### 3. Model Building
Multiple classification models were trained and evaluated:
- Logistic Regression

### 4. Evaluation Metrics
- Accuracy
- Precision, Recall, F1-Score
- Confusion Matrix
- ROC-AUC Curve

---
## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/kmanasagithub/ML_Projects.git
   cd ML_Projects/Loan_Approval_Project
   ```
2. **Create a virtual environment (optional but recommended)**
  ```bash
  python -m venv venv
  source venv/bin/activate        # On Windows: venv\Scripts\activate
  ```
3. **Install dependencies**
   ```bash
     pip install -r requirements.txt
   ```
4. **Launch the notebook**
   ```bash
    jupyter notebook notebooks/Loan_Approval.ipynb
   ```
---

### 📦 Requirements
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

---

### 💡 Key Insights
- Credit History is the strongest predictor of loan approval.
- Applicants with higher combined income have a significantly better approval rate.
- Semi-urban property area applicants show slightly higher approval rates.
- Handling class imbalance improved model recall for rejected loans.
