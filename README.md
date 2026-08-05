# ❤️ Heart Disease Prediction Using Machine Learning

## 📌 Overview

This project is a Machine Learning-based Heart Disease Prediction System that predicts the risk of developing **Coronary Heart Disease (CHD) within 10 years** based on patient health parameters.

The project uses a **Logistic Regression classification algorithm** to analyze medical attributes such as age, gender, cholesterol level, blood pressure, smoking habits, and glucose level to predict whether a person is at risk of heart disease.

The complete Machine Learning workflow includes data preprocessing, exploratory data analysis, feature scaling, model training, and performance evaluation.

---

## 🎯 Problem Statement

Heart disease is one of the leading causes of death worldwide. Early prediction of cardiovascular risk can help in preventive healthcare and timely medical decisions.

The objective of this project is to develop a Machine Learning model that can classify patients into two categories:

- **0 → No Heart Disease Risk**
- **1 → Heart Disease Risk**

based on their medical information.

---

# 🚀 Features

- Data loading and preprocessing
- Handling missing values
- Exploratory Data Analysis (EDA)
- Feature selection
- Feature scaling using StandardScaler
- Machine Learning model implementation
- Model evaluation using:
  - Accuracy Score
  - Classification Report
  - Confusion Matrix
- Data visualization using Matplotlib and Seaborn

---

# 🛠️ Technologies Used

### Programming Language
- Python

### Libraries & Frameworks

- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

# 📂 Project Structure

```
Heart-Disease-Prediction-ML/

│
├── dataset/
│   └── dataset.csv
│
├── notebooks/
│   └── main.ipynb
│
├── src/
│   └── main.py
│
├── README.md
│
├── requirements.txt
│
└── .gitignore
```

---

# 📊 Dataset Information

The dataset used in this project contains medical records of patients and their health-related attributes to predict the possibility of coronary heart disease.

## Features Used

| Feature | Description |
|---------|-------------|
| age | Age of the patient |
| Sex_male | Gender of the patient |
| cigsPerDay | Number of cigarettes consumed per day |
| totChol | Total cholesterol level |
| sysBP | Systolic blood pressure |
| glucose | Blood glucose level |

## Target Variable

| Target | Description |
|--------|-------------|
| TenYearCHD | 10-year risk of coronary heart disease |

Values:

- **0 → No Risk**
- **1 → Risk of Heart Disease**

---

# ⚙️ Machine Learning Workflow

The project follows these steps:

### 1. Data Collection
- Loaded the heart disease dataset using Pandas.

### 2. Data Preprocessing
- Removed unnecessary columns.
- Renamed features for better readability.
- Removed missing values.

### 3. Feature Selection
Selected important medical features:

- Age
- Gender
- Cigarettes per day
- Total cholesterol
- Systolic blood pressure
- Glucose level

### 4. Data Transformation

Applied feature scaling using:

```
StandardScaler()
```

to normalize feature values.

### 5. Train-Test Split

Dataset was divided into:

- Training Data → 70%
- Testing Data → 30%

### 6. Model Training

Implemented:

## Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for binary classification problems.

The model predicts whether a patient has a higher risk of developing heart disease.

---

# 📈 Model Evaluation

The model performance is evaluated using multiple metrics:

## Accuracy Score

Measures the percentage of correct predictions made by the model.

## Classification Report

Provides:

- Precision
- Recall
- F1-score

## Confusion Matrix

Shows:

- True Positives
- True Negatives
- False Positives
- False Negatives

---

# 📊 Exploratory Data Analysis

The project includes visual analysis to understand:

- Distribution of heart disease cases
- Class imbalance
- Relationship between patient attributes and heart disease risk

Visualizations are created using:

- Matplotlib
- Seaborn

---

# ▶️ How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Heart-Disease-Prediction-ML.git
```

## 2. Navigate to Project Directory

```bash
cd Heart-Disease-Prediction-ML
```

## 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run Python Script

```bash
python src/main.py
```

## 5. Run Jupyter Notebook

```bash
jupyter notebook
```

Open:

```
notebooks/main.ipynb
```

---

# 🔮 Future Improvements

Future enhancements that can improve this project:

- Implement additional Machine Learning algorithms:
  - Random Forest
  - XGBoost
  - Support Vector Machine
  - Gradient Boosting

- Perform hyperparameter optimization

- Handle class imbalance using techniques like SMOTE

- Deploy the model using:
  - Flask
  - FastAPI
  - Streamlit

- Build an interactive web application for real-time predictions

---

# 📌 Key Learnings

Through this project, I gained practical experience in:

- Data preprocessing
- Exploratory Data Analysis
- Feature engineering
- Machine Learning model development
- Model evaluation
- Healthcare predictive analytics

---

# 👨‍💻 Author

**Jay Rajput**

Aspiring Machine Learning Engineer | Data Scientist

GitHub: https://github.com/CEO-of-AJR

LinkedIn: https://linkedin.com/in/jax-r

---

⭐ If you found this project useful, consider giving it a star!
