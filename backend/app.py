from fastapi import FastAPI
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

# 1. Create the App instance (Our "Restaurant")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # This allows your React app to talk to the API
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Define a "Welcome" page
# When you visit http://127.0.0.1:8000/, this runs
@app.get("/")
def home():
    return {"message": "Welcome to the Investec Loan API!"}

# 3. Define the "Request Loan" page
# This is where the user sends their data
@app.post("/apply")
def apply_for_loan(name: str, score: int, income: float, expenses: float):
    # --- RUN THE BRAIN ---
    credit_points = (score / 850) * 100
    dti_ratio = (expenses / income)
    debt_points = (1 - dti_ratio) * 100
    final_score = (credit_points * 0.6) + (debt_points * 0.4)
    
    decision = "APPROVED" if final_score > 70 else "DECLINED"

    # --- SAVE TO THE DATABASE ---
    conn = sqlite3.connect('bank_records.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO applications (customer_name, credit_score, final_score, decision) VALUES (?, ?, ?, ?)",
        (name, score, round(final_score, 2), decision)
    )
    conn.commit()
    conn.close()

    # --- SEND THE RESULT BACK TO THE USER ---
    return {
        "customer": name,
        "final_score": round(final_score, 2),
        "status": decision
    }