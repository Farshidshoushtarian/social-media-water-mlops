# 🚰 Social Media Monitoring for Water Utilities 🌊  
*An End-to-End MLOps Pipeline using Hopsworks, GenAI, and FTI Architecture*

![License](https://img.shields.io/badge/Status-MVP%20In%20Progress-blue)  
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)  
![Hopsworks](https://img.shields.io/badge/Powered_by-Hopsworks-green)  
![MLOps](https://img.shields.io/badge/MLOps-End_to_End-orange)

---

## 📖 Project Overview
This project is an automated **MLOps pipeline** designed to help **water utilities** monitor and analyze public sentiment, service issues, and potential incidents by leveraging **social media data**.

🔹 Runs every **12 hours** to:
- Ingest posts from platforms like **Twitter/X**
- Perform **sentiment analysis**, **NER**, and **anomaly detection**
- Generate **GenAI-powered summaries**
- Trigger alerts and update a live dashboard

> 🎯 Built using modern MLOps practices, this project is also a portfolio piece demonstrating scalable, production-ready AI pipelines with **Hopsworks**, **GitHub Actions**, **Airflow**, and **Docker**.

---

## 🚀 Features
- ✅ Automated social media scraping (Twitter/X)
- ✅ Data preprocessing and feature engineering
- ✅ Centralized **Feature Store** using Hopsworks
- ✅ ML pipeline for Sentiment Analysis & Named Entity Recognition (NER)
- ✅ **GenAI summarization** (OpenAI API)
- ✅ Anomaly detection for complaint spikes
- ✅ Streamlit dashboard for real-time insights
- ✅ Alerts via email for critical issues
- ✅ CI/CD with GitHub Actions
- ✅ Containerized with Docker
- ✅ Orchestrated with Airflow

---

## 🏗️ Architecture

### FTI (Feature, Training, Inference) Design
```mermaid
graph TD
A[Social Media APIs] --> B[Feature Layer<br>Ingestion & Preprocessing]
B --> C[Hopsworks Feature Store]
C --> D[Training Layer<br>ML Pipelines + MLflow]
C --> E[Inference Layer<br>Batch Predictions + GenAI]
E --> F[Alerts & Dashboard]
```
---
---

## ⚙️ Tech Stack
| **Category**     | **Tools/Frameworks**              |
|------------------|-----------------------------------|
| Programming      | Python 3.10+                      |
| MLOps Platform   | Hopsworks, MLflow                 |
| Orchestration    | Apache Airflow, Cron              |
| AI/ML            | HuggingFace, spaCy, Scikit-learn  |
| GenAI            | OpenAI API                        |
| Dashboard        | Streamlit                         |
| Deployment       | Docker, GitHub Actions            |
| Data Versioning  | DVC                               |

---

## 📂 Repository Structure
```plaintext
├── data_ingestion/        # Social media scrapers & ETL scripts
├── feature_store/         # Feature engineering & Hopsworks integration
├── training/              # Model training pipelines (Sentiment, NER)
├── inference/             # Batch inference, GenAI summarization
├── dashboard/             # Streamlit app
├── airflow_dags/          # Orchestration workflows
├── docker/                # Docker configs
├── .github/               # GitHub Actions workflows
├── requirements.txt
├── README.md
└── LICENSE
```
---

## 🚧 Current Status
MVP in Progress
This project is under active development as a part-time initiative. Contributions and feedback are welcome!

---

## 📈 How It Works
1- Ingestion: Pulls relevant posts mentioning the utility every 12 hours.

2- Feature Layer: Processes text and stores structured data in Hopsworks.

3- Training Layer: ML models predict sentiment & extract entities.

4- Inference Layer: Generates summaries, detects anomalies, triggers alerts.

5- Visualization: Updates dashboard and sends reports.

---

## 🛠️ Setup Instructions

Follow these steps to set up and run the project locally.

### 1️⃣ Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/social-media-water-mlops.git
cd social-media-water-mlops
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure API Keys
Create a .env file:

```bash
TWITTER_API_KEY=your_key_here
REDDIT_CLIENT_ID=your_id_here
OPENAI_API_KEY=your_openai_key
HOPSWORKS_API_KEY=your_hopsworks_key
EMAIL_SMTP_SERVER=smtp.example.com
```

### 4️⃣ Run Ingestion Script
```bash
python data_ingestion/run_ingestion.py
```
---

## 📊 Example Output
(Example dashboard or report snapshot will be added here once available)

---
## 🤝 Potential Collaboration
This tool is designed with real-world utility use in mind. If you're a water utility interested in pilot testing, feel free to reach out via LinkedIn or open an issue!

---

## 🌟 Key Learnings & Challenges
Leveraged Hopsworks Feature Store for efficient feature management.

Integrated GenAI summarization for actionable reporting.

Implemented robust MLOps practices with CI/CD, orchestration, and monitoring.

Overcame challenges with API rate limits and social media data noise.

---

## 📝 License
This project is licensed under the MIT License.

---

## 🙌 Acknowledgments
Hopsworks

HuggingFace Transformers

OpenAI

Twitter Developer Platform

---

## 👨‍💻 About Me
I'm Farshid Shoushtarian, a quantitative scientist/engineer with expertise in AI/ML, MLOps, and the water industry. Passionate about leveraging data and automation to solve real-world water challenges.

👉 Connect with me on [LinkedIn](https://www.linkedin.com/in/farshid-shoushtarian-ph-d-7537b683/)
👉 Explore more projects at [GitHub](https://github.com/Farshidshoushtarian)


