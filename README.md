# 🏦 Mini FinTech Loan Scoring System

A full-stack credit risk assessment tool designed to simulate the decision-making engines used by major South African financial institutions.

## 🧠 The "Banking Brain" (Weighted Scoring)
Unlike simple "Yes/No" systems, this project uses a **Weighted Risk Model** to calculate creditworthiness. The system balances two primary factors:
* **Credit History (60% weight):** Normalized score based on the South African standard (0-850).
* **Financial Health (40% weight):** Calculated via Debt-to-Income (DTI) ratio.

**The Formula:** $Score = (Credit Points \times 0.6) + (Debt Points \times 0.4)$

## 🛠️ Tech Stack
* **Frontend:** React.js (State management & dynamic UI)
* **Backend:** Python with FastAPI (RESTful API & Business Logic)
* **Database:** SQLite (Persistent application storage)
* **Version Control:** Git/GitHub (Feature-branch workflow)

## 🏗️ System Architecture
* **Clean Separation:** Independent `/backend` and `/frontend` directories for scalability.
* **Persistence Layer:** Every application is logged in a SQL database for audit trails.
* **CORS Enabled:** Secure cross-origin communication between the React face and the Python heart.

## 🏃 How to Run
1. **Backend:**
   - `cd backend`
   - `uvicorn app:app --reload`
2. **Frontend:**
   - `cd frontend`
   - `npm start`

 