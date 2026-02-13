# 🌐 Website Fraud Detection System using Machine Learning

## 📌 Project Overview

The Website Fraud Detection System is an end-to-end Machine Learning pipeline designed to detect whether a website is legitimate or fraudulent based on various features. This project implements a complete ML lifecycle including data ingestion, validation, transformation, model training, evaluation, and tracking.

The system helps improve cybersecurity by identifying malicious websites and preventing potential fraud.

---

## 🎯 Objectives

- Detect fraudulent websites using Machine Learning
- Build a modular and scalable ML pipeline
- Automate training and evaluation process
- Track model performance
- Save trained models for future prediction

---

## 🧠 Machine Learning Pipeline Architecture

The project follows a modular pipeline structure:

Data Ingestion → Data Validation → Data Transformation → Model Training → Model Evaluation → Model Deployment


---

## 📂 Project Structure

websitefrauddetection/
│
├── networksecurity/
│ ├── components/
│ │ ├── data_ingestion.py
│ │ ├── data_validation.py
│ │ ├── data_transformation.py
│ │ └── model_trainer.py
│ │
│ ├── exception/
│ ├── logging/
│ ├── utils/
│ └── entity/
│
├── Artifacts/
│
├── main.py
├── requirements.txt
├── README.md
│
└── .github/workflows/main.yaml


---

## ⚙️ Technologies Used

- Python 3.10
- Scikit-learn
- Pandas
- NumPy
- MongoDB Atlas
- MLflow
- GitHub Actions
- YAML
- Machine Learning Algorithms:
  - Gradient Boosting
  - Random Forest
  - Logistic Regression
  - Decision Tree

---

## 🔄 Pipeline Components

### 1. Data Ingestion
- Fetches data from MongoDB Atlas
- Converts data into Pandas DataFrame
- Splits data into training and testing sets

### 2. Data Validation
- Validates schema
- Checks missing values
- Ensures data quality

### 3. Data Transformation
- Feature engineering
- Data scaling
- Data preprocessing

### 4. Model Trainer
- Trains multiple ML models
- Selects best model
- Evaluates performance
- Saves trained model

---

## 📊 Model Training Output

The model training shows:

- Train Loss decreasing
- Improved model performance
- Best model selected automatically

Example:

Iter Train Loss OOB Improve
1 1.35 0.014
100 0.67 0.002
200 0.47 0.001


---

## 💾 Artifacts Generated

Artifacts/
│
├── data_ingestion/
├── data_validation/
├── data_transformation/
└── model_trainer/
└── trained_model.pkl


---

## 🚀 How to Run the Project

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/websitefrauddetection.git
cd websitefrauddetection
Step 2: Create Virtual Environment
python -m venv myenv
Activate environment:

Windows:

myenv\Scripts\activate
Linux/Mac:

source myenv/bin/activate
Step 3: Install Requirements
pip install -r requirements.txt
Step 4: Run Pipeline
python main.py
☁️ MongoDB Integration
Data stored in MongoDB Atlas

Pipeline fetches data directly from cloud database

Ensures scalable data ingestion

📈 MLflow Integration
Tracks model performance

Logs metrics

Saves trained models

🔐 Use Cases
Fraud detection systems

Cybersecurity applications

Website trust analysis

Financial security systems

👨‍💻 Author
Varun Teja Mekala
B.Tech AIML Student
Machine Learning Developer

