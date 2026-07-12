# 🛡️ Insurance Premium Prediction System

An end-to-end Machine Learning project that predicts the **Insurance Premium Category** based on user information such as age, BMI, income, occupation, smoking habits, and city.

The project is built using **FastAPI** for the backend API, **Docker** for containerization, **Render** for backend deployment, and **Streamlit** for an interactive frontend.

---

## 🚀 Live Demo

### 🌐 Frontend (Streamlit)

https://insurance-premium-prediction-fastapi.streamlit.app/

### ⚡ Backend API (FastAPI)

https://insurance-premium-api-kxta.onrender.com

### 📄 API Documentation

https://insurance-premium-api-kxta.onrender.com/docs

---

# 📌 Features

- Predict Insurance Premium Category
- FastAPI REST API
- Interactive Streamlit UI
- Dockerized Backend
- Automatic API Documentation using Swagger UI
- Pydantic Data Validation
- Machine Learning Model Integration
- Responsive User Interface
- Cloud Deployment

---

# 🛠️ Tech Stack

## Backend

- FastAPI
- Python
- Pydantic
- Uvicorn

## Machine Learning

- Scikit-Learn
- Joblib
- Pandas
- NumPy

## Frontend

- Streamlit
- Requests

## Deployment

- Docker
- Render
- Streamlit Community Cloud

---

# 📂 Project Structure

```
Insurance-Premium-prediction-FastAPI/
│
├── config/
│   └── city_tier.py
│
├── model/
│   ├── model.pkl
│   └── predict.py
│
├── schema/
│   ├── user_input.py
│   └── prediction_response.py
│
├── frontend/
│   └── streamlit_app.py
│
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Ananya18-23/Insurance-Premium-prediction-FastAPI.git
```

```
cd Insurance-Premium-prediction-FastAPI
```

---

## Create Virtual Environment

```bash
python -m venv myenv
```

### Windows

```bash
myenv\Scripts\activate
```

### Linux / Mac

```bash
source myenv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Streamlit Frontend

```bash
streamlit run frontend/streamlit_app.py
```

---

# 🐳 Docker

## Build Image

```bash
docker build -t insurance-premium-api .
```

## Run Container

```bash
docker run -p 8000:8000 insurance-premium-api
```

---

# 📡 API Endpoint

## POST

```
/predict
```

### Request Example

```json
{
  "age": 28,
  "weight": 70,
  "height": 1.72,
  "income_lpa": 12,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

### Response Example

```json
{
  "predicted_category": "Medium"
}
```

---

# 🧠 Machine Learning Workflow

```
User Input
      │
      ▼
Pydantic Validation
      │
      ▼
Feature Engineering
      │
      ▼
Model Prediction
      │
      ▼
Insurance Premium Category
```

---

# ☁️ Deployment

### Backend

- FastAPI
- Docker
- Render

### Frontend

- Streamlit Community Cloud

---

# 📷 Project Preview

## Frontend

Streamlit Web Application

## Backend

FastAPI Swagger Documentation

---

# 👩‍💻 Author

**Ananya Ginnare**

B.Tech (Artificial Intelligence & Machine Learning)

GitHub:
https://github.com/Ananya18-23
---
