import pandas as pd
import mysql.connector

# Step 1: Load CSV (change filename if needed)
df = pd.read_csv("customer.csv")

# Step 2: Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mustafa(123)',      # ✅ Your actual MySQL password
    database='ccbbd'              # ✅ Your target database
)
cursor = conn.cursor()

# Step 3: Insert data into cust_detail
for _, row in df.iterrows():
    sql = """
    INSERT INTO cust_detail (
        Client_Num, Customer_Age, Gender, Dependent_Count,
        Education_Level, Marital_Status, State_cd, Zipcode,
        Car_Owner, House_Owner, Personal_Loan, Contact,
        Customer_Job, Income, Cust_Satisfaction_Score
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, tuple(row))

# Step 4: Finish
conn.commit()
cursor.close()
conn.close()

print("✅ customer.csv inserted into cust_detail successfully!")
