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
| Data Versioning  | DVC (optional)                    |

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

