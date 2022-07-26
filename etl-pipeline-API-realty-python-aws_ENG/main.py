from scripts.db_funcs import insert_into_mysql
from scripts.functions import *
from scripts.constants import *
from user_data import *
import pymysql
import os, sys, shutil

# Request data
print("Requesting sales data...")
try:
    sales = get_sales(CITY, STATE_CODE, LIMIT)
    sales = sales[SALES_COLS]
    print("Ok.")
except Exception as e:
    print(f"Error: {e}")
    sys.exit()

print("Requesting rents data...")
try:
    rents = get_rent(CITY, STATE_CODE, LIMIT)
    rents = rents[RENTS_COLS]
    print("Ok.")
except Exception as e:
    print(f"Error: {e}")
    sys.exit()

print("Requesting sold data...")
try:
    sold = get_sold(CITY, STATE_CODE, LIMIT)
    sold = sold[SOLD_COLS]
    print("Ok.")
except Exception as e:
    print(f"Error: {e}")
    sys.exit()


# Remove NAN values from dataframes
print("Removing NA values..\n")
try:
    sales = fill_na(sales)
    rents = fill_na(rents)
    sold = fill_na(sold)
    print("Ok.")
except Exception as e:
    print(f"Error: {e}")
    sys.exit()


# For backup purpose, save dataframes into csv files
try:
    if not os.path.exists("./csv/"):
        print("Creating csv folder...")
        os.makedirs("./csv/")
    else:
        print("Csv folder already exists, removing and creating and empty one...")
        shutil.rmtree("./csv/", ignore_errors=True)
        os.makedirs("./csv/")
    print("Saving data into csv files..")
    sales.to_csv("./csv/sales.csv", index=False)
    rents.to_csv("./csv/rents.csv", index=False)
    sold.to_csv("./csv/sold.csv", index=False)
    print("Ok.")
except Exception as e:
    print(f"Error: {e}")
    sys.exit()

# sales = pd.read_csv("sales.csv")
# rents = pd.read_csv("rents.csv")
# sold = pd.read_csv("sold.csv")

# Fill these data with your credentials
host = 'localhost'
host_aws = 'db-realty.ctu8ks44oyou.us-east-1.rds.amazonaws.com'
port = 3306
user = 'user'
password = 'userpass'


# Create a connection with the database service in local machine
print("Connecting to the database...")
try:
    con = pymysql.connect(host=host, port=port, user=user, passwd=password)
    print(f"Success: {con}")
except Exception as e:
    print(f"Error connecting to db: {e}")
    sys.exit()

# Creating a cursor object
cursor = con.cursor()

# Use the realty schema
cursor.execute('''
    USE realty;
''')

# Insert data into MySQL
print("Inserting data..")
try:
    print("into sales table..")
    insert_into_mysql(cursor, sales, "sales")

    print("into rents table..")
    insert_into_mysql(cursor, rents, "rents")

    print("into sold table..\n")
    insert_into_mysql(cursor, sold, "sold")

    print("Done.\n")
except Exception as e:
    print(f"Error inserting data: {e}")
    sys.exit()


# Querying sample data
query = '''
        SELECT * FROM sales LIMIT 5;
'''
cursor.execute(query)
result = cursor.fetchall()

print("Sample of the data: \n")
print(result)

# Commit
con.commit()
con.close()


