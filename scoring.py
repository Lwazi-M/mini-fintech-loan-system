# --- THE BANK GUARD'S LOGIC ---

# 1. We ask the user for their information (Inputs)
# Think of this like filling out a form at Standard Bank
credit_score = 650
monthly_income = 15000
monthly_expenses = 4000

# 2. We calculate the "Leftover Money"
# This is what's left after you pay for food and rent
leftover_money = monthly_income - monthly_expenses

# 3. The Decision Logic (The "IF" statements)
# We check if the credit score is good AND if they have enough money left
if credit_score > 600 and leftover_money > 5000:
    # If both are true, they win!
    print("Congratulations! Your loan is APPROVED. ✅")
else:
    # If even one is false, they are declined
    print("Sorry, your loan was DECLINED. ❌")
    
# 4. Show the math so the user understands why
print("Reasoning:")
print("Your leftover money is: R", leftover_money)