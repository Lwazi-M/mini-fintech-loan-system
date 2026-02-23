import sqlite3

# 1. Open the 'Bank Filing Cabinet'
connection = sqlite3.connect('bank_records.db')
cursor = connection.cursor()

# 2. Ask for the data
# '*' means 'Everything' (All columns: ID, Name, Score, etc.)
cursor.execute("SELECT * FROM applications")

# 3. Get all the rows
# Think of 'fetchall()' like grabbing all the files from the shelf
all_apps = cursor.fetchall()

print("--- 🏦 BANK APPLICATION LOG 🏦 ---")
print(f"{'ID':<5} {'Name':<15} {'Score':<10} {'Status':<10}")
print("-" * 45)

# 4. Loop through the list and print them nicely
# In CAT, this is like viewing rows in a table
for app in all_apps:
    # app[0] is ID, app[1] is Name, app[3] is Score, app[4] is Decision
    print(f"{app[0]:<5} {app[1]:<15} {app[3]:<10} {app[4]:<10}")

# 5. Clean up
connection.close()