import sqlite3

def run_report():
    conn = sqlite3.connect('bank_records.db')
    cursor = conn.cursor()

    # 1. Count Total Applications
    cursor.execute("SELECT COUNT(*) FROM applications")
    total = cursor.fetchone()[0]

    # 2. Count Approved vs. Declined
    cursor.execute("SELECT decision, COUNT(*) FROM applications GROUP BY decision")
    results = dict(cursor.fetchall())

    # 3. Calculate Average Score
    cursor.execute("SELECT AVG(final_score) FROM applications")
    avg_score = cursor.fetchone()[0]

    print("--- 🏦 INVESTEC LOAN SYSTEM: SUMMARY REPORT ---")
    print(f"Total Applications Processed: {total}")
    print(f"✅ Approved: {results.get('APPROVED', 0)}")
    print(f"❌ Declined: {results.get('DECLINED', 0)}")
    print(f"📈 Average Financial Health Score: {round(avg_score, 2)}%")
    print("-" * 46)

    conn.close()

if __name__ == "__main__":
    run_report()