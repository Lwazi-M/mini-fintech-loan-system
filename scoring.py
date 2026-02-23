import sqlite3

# --- 1. COLLECTING DATA (The Digital Form) ---
print("--- 🏦 Investec Loan Entry System ---")

# We use input() to let YOU type in the terminal
customer_name = input("Enter Customer Name: ")

# We use int() because the computer needs to know these are numbers, not just text
credit_score = int(input("Enter Credit Score (0-850): "))
monthly_income = float(input("Enter Monthly Income (R): "))
monthly_expenses = float(input("Enter Monthly Expenses (R): "))

# --- 2. THE BRAIN (Math Logic) ---
# (Same math as before, but now using your inputs!)
credit_points = (credit_score / 850) * 100
dti_ratio = (monthly_expenses / monthly_income)
debt_points = (1 - dti_ratio) * 100

final_score = (credit_points * 0.6) + (debt_points * 0.4)

if final_score > 70:
    decision = "APPROVED"
else:
    decision = "DECLINED"

# --- 3. THE MEMORY (Saving to SQL) ---
connection = sqlite3.connect('bank_records.db')
cursor = connection.cursor()

sql_command = "INSERT INTO applications (customer_name, credit_score, final_score, decision) VALUES (?, ?, ?, ?)"
data_to_save = (customer_name, credit_score, round(final_score, 2), decision)

cursor.execute(sql_command, data_to_save)
connection.commit()
connection.close()

print(f"\n✅ Success! {customer_name}'s application has been recorded.")
print(f"Final Score: {round(final_score, 2)} | Decision: {decision}")