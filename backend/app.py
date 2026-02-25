from fastapi import FastAPI, HTTPException
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

# 1. Create the App instance
app = FastAPI()

# 2. Enable CORS so React (port 3000) can talk to FastAPI (port 8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to the Investec Loan API!"}

@app.post("/apply")
def apply_for_loan(name: str, score: int, income: float, expenses: float):
    # --- 3. SAFETY CHECKS (Validation) ---
    # We stop the process early if the data is "garbage"
    if score < 0 or score > 850:
        raise HTTPException(status_code=400, detail="Credit score must be between 0 and 850")
    
    if income <= 0:
        raise HTTPException(status_code=400, detail="Monthly income must be a positive number")

    if expenses < 0:
        raise HTTPException(status_code=400, detail="Expenses cannot be negative")

    # --- 4. RUN THE BRAIN (Scoring Logic) ---
    credit_points = (score / 850) * 100
    
    # Calculate DTI (Debt-to-Income)
    dti_ratio = (expenses / income)
    
    # If expenses are higher than income, debt_points could go negative. 
    # We use max(0, ...) to ensure the lowest score is 0.
    debt_points = max(0, (1 - dti_ratio) * 100)
    
    # Weighted calculation: 60% Credit, 40% Financial Health
    final_score = (credit_points * 0.6) + (debt_points * 0.4)
    
    decision = "APPROVED" if final_score > 70 else "DECLINED"

    # --- 5. SAVE TO THE DATABASE ---
    try:
        conn = sqlite3.connect('bank_records.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO applications (customer_name, credit_score, final_score, decision) VALUES (?, ?, ?, ?)",
            (name, score, round(final_score, 2), decision)
        )
        conn.commit()
        conn.close()
    except sqlite3.OperationalError:
        # If you forgot to run database_setup.py, this will catch it
        raise HTTPException(status_code=500, detail="Database table not found. Run setup script.")

    # --- 6. SEND THE RESULT BACK ---
    return {
        "customer": name,
        "final_score": round(final_score, 2),
        "status": decision
    }