# 🏠 House Price Prediction using Linear Regression

## 📌 Project Overview
This project predicts house prices using **Machine Learning (Linear Regression)**.
The model learns relationships between house features such as area, year built, zoning type, and basement size to estimate the final sale price.

Built using:
- Python
- Google Colab
- Scikit-learn
- Pandas
- NumPy
- Matplotlib

---

## 🎯 Problem Statement
Given various house attributes, predict the **SalePrice** of a house.

This is a **Supervised Regression Problem** because:
- Input → House features
- Output → Continuous value (price)

---

## 📂 Dataset Information
The dataset contains **2900+ houses** with multiple structural and location-based features.

### Target Variable
| Column | Description |
|--------|-------------|
| SalePrice | Final house selling price (what we predict) |

### Features Used

| Feature | Description |
|-----------|-------------|
| Id | Unique house ID |
| MSSubClass | Type of dwelling |
| MSZoning | Zoning classification (RL, RM, etc.) |
| LotArea | Lot size (sq ft) |
| LotConfig | Lot configuration (Corner, Inside, etc.) |
| BldgType | Building type |
| OverallCond | Overall condition rating |
| YearBuilt | Construction year |
| YearRemodAdd | Remodel year |
| Exterior1st | Exterior covering |
| BsmtFinSF2 | Basement finished area |
| TotalBsmtSF | Total basement area |

---

## ⚙️ Steps Performed

### 1️⃣ Data Preprocessing
- Removed unnecessary columns
- Handled missing values
- Converted categorical features using:
  - One-Hot Encoding (`pd.get_dummies()`)
- Feature scaling (if applied)

### 2️⃣ Train-Test Split
```python
train_test_split(test_size=0.2)
````

### 3️⃣ Model Building
Used:
```python
LinearRegression()
```

### 4️⃣ Model Training
```python
model.fit(X_train, y_train)
```

### 5️⃣ Prediction
```python
y_pred = model.predict(X_test)
```

### 6️⃣ Evaluation Metrics
* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)

## 🛠️ Installation & Usage

### Step 1
Clone repo
```bash
git clone https://github.com/kmanasagithub/ML_Projects.git
```

### Step 2
Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3
Run notebook
Open:
```
HousePrice_Prediction_Using_Linear_Regression.ipynb
```

## 📦 Requirements
Create `requirements.txt`
```
pandas
numpy
matplotlib
scikit-learn
jupyter
```

⭐ If you like this project, give it a star!
