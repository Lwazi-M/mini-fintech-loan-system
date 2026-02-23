import sqlite3  # Import the tool to talk to the database

# --- 1. THE MATH ENGINE (The Brain) ---
customer_name = "Nhlanzeko" # We'll make this dynamic later!
credit_score = 720
monthly_income = 25000
monthly_expenses = 8000

# Normalizing scores (Same math as before)
credit_points = (credit_score / 850) * 100
dti_ratio = (monthly_expenses / monthly_income)
debt_points = (1 - dti_ratio) * 100

# Final Weighted Score (60% Credit, 40% Debt)
final_score = (credit_points * 0.6) + (debt_points * 0.4)

if final_score > 70:
    decision = "APPROVED"
else:
    decision = "DECLINED"

# --- 2. THE SAVING ENGINE (The Memory) ---

# Connect to our 'bank_records.db' file
connection = sqlite3.connect('bank_records.db')
cursor = connection.cursor()

# Prepare the SQL command: "Insert these details into the table"
# The '?' are placeholders to keep things safe and organized
sql_command = "INSERT INTO applications (customer_name, credit_score, final_score, decision) VALUES (?, ?, ?, ?)"
data_to_save = (customer_name, credit_score, round(final_score, 2), decision)

# Execute (Do the work) and Commit (Save it permanently)
cursor.execute(sql_command, data_to_save)
connection.commit()

# Always close the connection when done!
connection.close()

print(f"Application for {customer_name} processed and saved to the database! 🏦")