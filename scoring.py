# --- THE ADVANCED BANKING BRAIN ---

# 1. Inputs (The data we get from the user)
credit_score = 720  # Out of 850
monthly_income = 25000
monthly_expenses = 8000

# 2. Weights (How important each thing is - Total must be 1.0 or 100%)
# Banks like Investec value credit history very highly
credit_weight = 0.6 
debt_weight = 0.4

# 3. Normalizing the scores (Turning them into a mark out of 100)
# Credit: (Your Score / Max Score) * 100
credit_points = (credit_score / 850) * 100

# Debt: If you spend 0, you get 100 points. If you spend everything, you get 0.
dti_ratio = (monthly_expenses / monthly_income)
debt_points = (1 - dti_ratio) * 100

# 4. The Final Weighted Calculation
# (Point A * Weight A) + (Point B * Weight B)
final_score = (credit_points * credit_weight) + (debt_points * debt_weight)

# 5. The Output
print(f"--- FinTech Loan Analysis ---")
print(f"Credit Points: {round(credit_points, 2)}/100")
print(f"Debt Points: {round(debt_points, 2)}/100")
print(f"Overall Financial Health Score: {round(final_score, 2)}")

if final_score > 70:
    print("Decision: APPROVED ✅")
elif final_score > 50:
    print("Decision: REQUIRES MANUAL REVIEW ⚠️")
else:
    print("Decision: DECLINED ❌")