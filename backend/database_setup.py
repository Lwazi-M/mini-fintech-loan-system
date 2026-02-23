import sqlite3 # This is the library that lets Python talk to SQL

# 1. Connect to the Database
# This creates a file named 'bank_records.db' if it doesn't exist
connection = sqlite3.connect('bank_records.db')

# 2. Create a 'Cursor'
# Think of this like a pen that we use to write on the database
cursor = connection.cursor()

# 3. Create the Table
# We use BIG CAPITAL LETTERS for SQL commands to keep it clear
cursor.execute('''
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT,
        credit_score INTEGER,
        final_score REAL,
        decision TEXT
    )
''')

# 4. Save and Close
# In SQL, you must 'commit' to save your changes, like clicking 'Save' in Word
connection.commit()
connection.close()

print("Database and 'Applications' table created successfully! 🏦")