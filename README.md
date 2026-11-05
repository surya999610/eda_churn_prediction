# 📞 Telecom Customer Churn Prediction

### Machine Learning | Exploratory Data Analysis | Random Forest | Streamlit

An end-to-end Machine Learning project that analyzes telecom customer data and predicts whether a customer is likely to leave a service. The project uses Exploratory Data Analysis (EDA), data preprocessing, and a Random Forest Classifier to identify potential customer churn and estimate churn probability.

<p align="center">
  <a href="https://edachurnprediction.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀_Live_Demo-Open_App-success?style=for-the-badge" alt="Live Demo">
  </a>
  <a href="https://github.com/surya999610/eda_churn_prediction">
    <img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github" alt="GitHub">
  </a>
</p>

---

## 🚀 Live Application

**Try the deployed application here:**

🔗 https://edachurnprediction.streamlit.app/

The application allows users to enter telecom customer information and receive a prediction indicating whether the customer has a high or low risk of churn, along with the estimated churn probability.

---

## 📌 Project Overview

Customer churn is one of the major challenges faced by telecom companies. Losing existing customers can negatively impact revenue and business growth.

The objective of this project is to develop a Machine Learning model that identifies customers who are more likely to leave a telecom service.

Using customer demographic information, account details, and usage patterns, the model predicts churn risk and helps businesses understand customer retention opportunities.

### Key Objectives

- Perform Exploratory Data Analysis (EDA) to understand customer behavior.
- Clean and preprocess the dataset.
- Analyze customer characteristics and usage patterns.
- Prepare features for Machine Learning.
- Train a Random Forest Classification model.
- Predict customer churn and estimate churn probability.
- Deploy an interactive prediction application using Streamlit.

---

## 🛠️ Technologies & Tools

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computations |
| Matplotlib | Data visualization |
| Seaborn | Statistical data visualization |
| Plotly | Interactive visualizations |
| Scikit-learn | Machine Learning and preprocessing |
| Random Forest | Classification algorithm |
| Imbalanced-learn | Handling imbalanced datasets during training |
| Joblib | Saving and loading the trained model |
| Streamlit | Interactive web application |
| Jupyter Notebook | Data analysis and model development |
| Git & GitHub | Version control and project hosting |

---

## 📂 Project Structure

```text
eda_churn_prediction/
│
├── app.py
│   └── Streamlit application for churn prediction
│
├── eda-churn-prediction.ipynb
│   └── Exploratory Data Analysis and model development
│
├── telecom_churn.csv
│   └── Telecom customer dataset
│
├── random_forest_churn_model.pkl
│   └── Trained Random Forest model
│
├── requirements.txt
│   └── Project dependencies
│
└── README.md
    └── Project documentation
```

---

## 🔄 Project Workflow

The project follows a complete Machine Learning workflow, starting from raw customer data and ending with a deployed prediction application.

### 1. Data Collection

The project uses a telecom customer dataset containing information about customer demographics, registration, location, and service usage.

### 2. Exploratory Data Analysis (EDA)

Performed exploratory analysis to understand the dataset and identify meaningful patterns.

Key activities:
- Understanding dataset structure and dimensions.
- Checking data types and statistical summaries.
- Identifying missing values and duplicate records.
- Analyzing numerical and categorical features.
- Studying customer behavior and churn distribution.
- Exploring relationships between customer attributes and churn.

### 3. Data Preprocessing

Prepared the dataset for Machine Learning.

Activities include:
- Handling missing values.
- Removing duplicate records where applicable.
- Encoding categorical variables.
- Preparing numerical features.
- Creating relevant features from existing columns.
- Preparing the target variable for classification.

### 4. Feature Engineering

Created additional features to improve the representation of customer information.

Examples include:

- **Age Group:** Categorizing customers based on age.
- **Registration Month:** Extracting the month from registration date.
- **Registration Year:** Extracting the year from registration date.

### 5. Handling Class Imbalance

Used RandomOverSampler from the Imbalanced-learn library to address class imbalance in the training data.

This helps provide the model with a more balanced representation of customer churn classes during training.

### 6. Model Training

Implemented a Random Forest Classifier using Scikit-learn.

Random Forest is an ensemble learning algorithm that combines multiple decision trees to generate classification predictions.

The trained model is used to classify customers into churn and non-churn categories.

### 7. Model Evaluation

The model can be evaluated using classification metrics such as:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

These metrics help evaluate the model's ability to identify customers at risk of leaving.

### 8. Model Deployment

The trained model is saved as a `.pkl` file using Joblib.

A Streamlit application loads the saved model and provides an interactive interface where users can enter customer information and receive predictions.

---

## 🤖 Machine Learning Model

**Algorithm:** Random Forest Classifier

Random Forest is an ensemble-based supervised Machine Learning algorithm used for classification and regression tasks.

In this project, it is used to predict whether a telecom customer is likely to leave the service.

### Input Features

The deployed application accepts the following customer information:

| Category | Features |
|---|---|
| Account Information | Telecom Partner, Registration Date |
| Demographics | Gender, Age, Number of Dependents |
| Location | State, City |
| Financial Information | Estimated Salary |
| Usage Metrics | Calls Made, SMS Sent, Data Used |

### Prediction Output

The application provides two possible prediction outcomes:

- **High Risk of Churn:** The customer is predicted to leave the service.
- **Low Risk of Churn:** The customer is predicted to stay with the service.

It also displays the estimated churn probability as a percentage.

---

## 🌐 Streamlit Application

The Machine Learning model is integrated into an interactive Streamlit web application.

### Application Features

- Interactive customer information form.
- Telecom partner selection.
- Customer demographic inputs.
- Location and registration information.
- Customer usage metrics.
- Real-time churn prediction.
- Churn probability displayed as a percentage.
- User-friendly prediction results.

### Try the Application

🔗 **Live Demo:** https://edachurnprediction.streamlit.app/

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/surya999610/eda_churn_prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd eda_churn_prediction
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
.\venv\Scripts\Activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

**Note:** The application requires the trained model file `random_forest_churn_model.pkl` in the project directory. Ensure the file is available before running the application.

---

## 📦 Requirements

The main dependencies are:

```text
streamlit
pandas
numpy
scikit-learn
joblib
```

Additional libraries used during analysis include Matplotlib, Seaborn, Plotly, and Imbalanced-learn.

---

## 🎯 Project Outcomes

- Developed an end-to-end customer churn prediction workflow.
- Performed exploratory data analysis on telecom customer data.
- Applied preprocessing and feature engineering techniques.
- Used Random Forest for customer churn classification.
- Addressed class imbalance using RandomOverSampler.
- Integrated the trained model into a Streamlit application.
- Deployed the application for interactive customer churn prediction.

---

## 🔮 Future Improvements

- Experiment with additional classification algorithms such as XGBoost and Gradient Boosting.
- Perform hyperparameter tuning to improve model performance.
- Add detailed model evaluation visualizations.
- Implement feature importance analysis.
- Develop a customer retention recommendation system.
- Improve prediction monitoring and model interpretability.

---

## 👨‍💻 Author

**Surya Gautam**

Data Science and Machine Learning Enthusiast

- GitHub: https://github.com/surya999610
- LinkedIn: https://www.linkedin.com/in/surya-gautam-03bba6286/

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**Thank you for visiting my project!**
