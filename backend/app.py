from fastapi import FastAPI, HTTPException
import sqlite3
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# --- 1. SELF-HEALING DATABASE SETUP ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This code runs on startup
    conn = sqlite3.connect('bank_records.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            credit_score INTEGER NOT NULL,
            final_score REAL NOT NULL,
            decision TEXT NOT NULL,
            applied_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    yield
    # Code here would run on shutdown (if needed)

# --- 2. Create the App instance with Lifespan ---
app = FastAPI(lifespan=lifespan)

# 3. Enable CORS so React (port 3000) can talk to FastAPI (port 8000)
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
    # --- 4. SAFETY CHECKS (Validation) ---
    if score < 0 or score > 850:
        raise HTTPException(status_code=400, detail="Credit score must be between 0 and 850")
    
    if income <= 0:
        raise HTTPException(status_code=400, detail="Monthly income must be a positive number")

    if expenses < 0:
        raise HTTPException(status_code=400, detail="Expenses cannot be negative")

    # --- 5. RUN THE BRAIN (Scoring Logic) ---
    credit_points = (score / 850) * 100
    dti_ratio = (expenses / income)
    debt_points = max(0, (1 - dti_ratio) * 100)
    
    final_score = (credit_points * 0.6) + (debt_points * 0.4)
    decision = "APPROVED" if final_score > 70 else "DECLINED"

    # --- 6. SAVE TO THE DATABASE ---
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
        raise HTTPException(status_code=500, detail="Database table issue. Please check Railway logs.")

    # --- 7. SEND THE RESULT BACK ---
    return {
        "customer": name,
        "final_score": round(final_score, 2),
        "status": decision
    }