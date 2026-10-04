import sqlite3
import csv
import os

DB_PATH = os.path.join('..', 'data', 'meesho_reseller.db')
OUTPUT_DIR = 'output'

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def execute_and_save(query, output_filename):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    headers = [description[0] for description in cur.description]
    conn.close()

    with open(os.path.join(OUTPUT_DIR, output_filename), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

q1 = """
SELECT month, category, ROUND(SUM(quantity * unit_price), 2) AS revenue, COUNT(*) AS n_orders
FROM orders
GROUP BY month, category
ORDER BY CASE month WHEN 'April' THEN 1 WHEN 'May' THEN 2 WHEN 'June' THEN 3 END, category;
"""

q2 = """
SELECT r.region, ROUND(SUM(o.quantity * o.unit_price), 2) AS total_revenue, COUNT(o.order_id) AS total_orders
FROM resellers r
JOIN orders o ON r.reseller_id = o.reseller_id
GROUP BY r.region
ORDER BY total_revenue DESC;
"""

q3 = """
SELECT r.reseller_id, r.reseller_name, ROUND(SUM(o.quantity * o.unit_price), 2) AS total_spend
FROM resellers r
JOIN orders o ON r.reseller_id = o.reseller_id
GROUP BY r.reseller_id, r.reseller_name
HAVING total_spend > 50000
ORDER BY total_spend DESC
LIMIT 5;
"""

q4 = """
SELECT r.reseller_id, r.reseller_name, COUNT(*) AS count_star, COUNT(o.order_id) AS count_order_id
FROM resellers r
LEFT JOIN orders o ON r.reseller_id = o.reseller_id
WHERE o.order_id IS NULL
GROUP BY r.reseller_id, r.reseller_name;
"""

q5 = """
SELECT ROUND(SUM(quantity * unit_price) / COUNT(*), 2) AS aov
FROM orders
WHERE month = 'June' AND status = 'Delivered';
"""

execute_and_save(q1, "monthly_category_revenue.csv")
execute_and_save(q2, "region_wise_revenue.csv")
execute_and_save(q3, "top_resellers.csv")
execute_and_save(q4, "inactive_resellers.csv")
execute_and_save(q5, "june_delivered_aov.csv")
print("SQL queries executed and outputs saved.")