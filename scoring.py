# --- THE SMARTER BANK GUARD (RISK SCORING) ---

# Inputs (Imagine these are from a bank's online form)
monthly_income = 20000
monthly_expenses = 5000

# 1. We calculate the Debt-to-Income Ratio (DTI)
# Analogy: How much of your "pie" is eaten by bills?
# We multiply by 100 to get a percentage (%)
dti_ratio = (monthly_expenses / monthly_income) * 100

# 2. Logic to determine the "Risk Level"
# In CAT, think of this like an 'IF' formula in Excel
if dti_ratio < 30:
    risk_level = "LOW"
    message = "You are a safe bet! ✅"
elif dti_ratio <= 50:
    risk_level = "MEDIUM"
    message = "We can help you, but be careful. ⚠️"
else:
    risk_level = "HIGH"
    message = "Sorry, you have too much debt. ❌"

# 3. Output the result
print(f"Your Debt Ratio is: {dti_ratio}%")
print(f"Calculated Risk: {risk_level}")
print(f"Bank Decision: {message}")