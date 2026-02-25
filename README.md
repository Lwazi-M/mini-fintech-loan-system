# 🏦 Mini FinTech Loan Scoring System

A professional, full-stack credit risk assessment engine designed to simulate the decision-making workflows of South African financial institutions like Investec, Discovery Bank, and Standard Bank.

## 🧠 The "Banking Brain" (Weighted Scoring)
Unlike simple "Yes/No" systems, The system uses a Weighted Heuristic Engine to determine creditworthiness, moving beyond simple binary logic to provide a nuanced "Financial Health Score":

* **Credit History (60% weight):** Normalizes the South African standard credit score (0-850) to generate a weighted component of the final score.

* **Financial Health (40% weight):** Utilizes Debt-to-Income (DTI) ratios to assess current liquidity and repayment capacity.

**The Formula:** $Score = (Credit Points \times 0.6) + (Debt Points \times 0.4)$

* **Data Validation:** Implements strict backend input sanitization to ensure credit scores (0-850) and financial figures are realistic and safe for processing.

* **Explainable Decisions:** Provides real-time feedback on "Approved" vs. "Declined" status based on weighted thresholds.

## 🛠️ Tech Stack
* **Frontend:** React.js featuring a dynamic Risk Gauge and real-time state management for immediate user feedback.

* **Backend:** Python with FastAPI serving as a RESTful API layer with CORS middleware for secure cross-origin communication.

* **Database:** SQLite persistence layer used for recording every application, ensuring an immutable audit trail.

* **Version Control:** Git/GitHub (Feature-branch workflow)

## 🏗️ System Architecture
* **Clean Separation:** Independent `/backend` and `/frontend` directories for scalability.
* **Persistence Layer:** Every application is logged in a SQL database for audit trails.
* **CORS Enabled:** Secure cross-origin communication between the React face and the Python heart.

## 🚀 Engineering & Reliability
To ensure this system is "bank-ready," the following engineering practices were implemented:

* **Stress Testing:** A custom Python utility (stress_test.py) was developed to simulate high-traffic scenarios, successfully processing 100+ concurrent applications without failure.

* **Automated Reporting:** A management-level script (generate_report.py) provides high-level data analytics, calculating pass rates and average financial health across the entire database.

* **Secure Coding:** Utilization of SQL placeholders to mitigate SQL Injection risks, a standard requirement for financial software.

## 🏃 How to Run
1. **Backend:**
   - `cd backend`
   - `uvicorn app:app --reload`
2. **Frontend:**
   - `cd frontend`
   - `npm start`

 