# 🌸 FloraPulse: High-Availability Iris Species Classification & FastAPI Gateway

[![Production Status](https://img.shields.io/badge/Production-Ready-emerald?style=flat-square)](#)
[![System Framework](https://img.shields.io/badge/Framework-FastAPI%20%7C%20Scikit--Learn-0369a1?style=flat-square)](#)
[![Python Version](https://img.shields.io/badge/Python-3.12-ba8fff?style=flat-square)](#)

FloraPulse is an enterprise-grade biological variant classification engine designed to map continuous morphological characteristics into discrete target species classifications (*Iris setosa*, *Iris versicolor*, and *Iris virginica*). Powered by an optimized Random Forest Ensemble, the system exposes scalable REST endpoints via an asynchronous FastAPI gateway for sub-millisecond real-time inference routing.

---

## 👥 Student & Developer Specification
* **Student Name:** Anushay Ayat
* **Student ID:** 773317
* **Institutional Department:** Artificial Intelligence & Data Science (SMIT)
* **Project Track:** Advanced Machine Learning Engineering & Production Deployment

---

## 🗺️ System Architecture Workflow
The operational execution of the FloraPulse pipeline follows a strict modular matrix layout:

1. **Environment Initialization:** Allocation of local socket runtimes and ingestion of core deployment servers (`FastAPI`, `Uvicorn`).
2. **Data Pipeline Ingestion:** Loading authentic multi-dimensional vector spaces from the Scikit-Learn data layer.
3. **Stratified Matrix Splitting:** Partitioning data arrays into a balanced 80% Training set and a 20% Validation pool.
4. **Ensemble Optimization:** Training a 100-tree Random Forest Classifier to achieve optimal class separation.
5. **Artifact Serialization:** Exporting the immutable trained model state into a binary byte-stream (`.pkl`) layer using Joblib.
6. **Asynchronous API Gateway:** Constructing Pydantic validation schemas and configuring GET/POST execution routing logic.
7. **Production Handshake:** Spawning background server daemons and verifying live inference transactions.

---

## ⚙️ Core Technical Tech Stack
* **Core Language:** Python 3.12
* **Predictive Modeling:** Scikit-Learn Ecosystem
* **Binary Serialization:** Joblib Engine
* **API Delivery Layer:** FastAPI (ASGI Specification)
* **Asynchronous Web Server:** Uvicorn Daemon
* **Client Handshake Interface:** Requests / Native JSON Arrays

---

## 🚀 Local Installation & Deployment Guide

Follow these sequential steps to initialize the FloraPulse gateway interface on your local workstation environment:

### 1. Project Directory Configuration
Ensure your root project directory layout matches the verified structural blueprint below:
```text
FloraPulse-Iris-Classification-API/
├── app.py
├── iris_random_forest_model.pkl
├── Iris_Classification_Production_API.ipynb
├── requirements.txt
└── README.md
```
---

### 2. Ingest System Dependencies
Install all production-grade package specifications isolated within the active environment layer:

```
pip install -r requirements.txt
```

### 3. Initialize the ASGI Production Server
Spin up the high-availability Uvicorn server socket pointing directly to the FastAPI application core:

```
uvicorn app:app --reload
```
***Expected Server Initialization Log:***
```
INFO:     Started server process [12480]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on [http://127.0.0.1:8000](http://127.0.0.1:8000) (Press CTRL+C to quit)
```

## 🧪 Interactive API Endpoint Handshake Specs
### 📡 Endpoint 1: Health Diagnostic Handshake
* **Protocol HTTP Method: GET**

* **Network URI Location: http://127.0.0.1:8000/**

* **Target Application Response:**
```{
  "status": "online",
  "message": "Welcome to the Vanguard Systems Iris Species Classification API Gateway!"
}
```

### 📡 Endpoint 2: Real-Time Model Inference Gateway
* **Protocol HTTP Method: POST**

 **Network URI Location: http://127.0.0.1:8000/predict**

* **Client Verification JSON Payload Request:**

```
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```
* ***Server Automated Response Package:***
```
{
  "prediction": "setosa"
}
```
## 📑 Automated Documentation Gateway
The complete API structure is documented programmatically. While the local server instance is active, you can access the self-documenting interface at:

* Interactive Swagger UI: http://127.0.0.1:8000/docs

* Alternative ReDoc Ecosystem: http://127.0.0.1:8000/redoc

***Developed under the technical instructional guidance of SMIT Artificial Intelligence and Data Science Faculty Core.***
