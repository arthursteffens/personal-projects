import pandas as pd
from functions import get_rent, get_sales, get_sold, fill_na
from constants import *
import pymysql

# Request data

sales = get_sales("New York City", "NY", "200")
sales = sales[SALES_COLS]
print(sales.head(5))

rents = get_rent("New York City", "NY", "200")
rents = rents[RENTS_COLS]
print(rents.head(5))

sold = get_sold("New York City", "NY", "200")
sold = sold[SOLD_COLS]
print(sold.head(5))


# Remove NAN values from dataframes
sales = fill_na(sales)
rents = fill_na(rents)
sold = fill_na(sold)


# Check if there are NAN values
print(f"{sales.isna().sum()} NA values")


# For backup purpose, save dataframes into csv files
sales.to_csv("./csv/sales.csv", index=False)
rents.to_csv("./csv/rents.csv", index=False)
sold.to_csv("./csv/sold.csv", index=False)


# sales = pd.read_csv("sales.csv")
# rents = pd.read_csv("rents.csv")
# sold = pd.read_csv("sold.csv")

# Fill these data with your credentials
host = 'localhost'
port = 3306
user = 'arthur'
password = 'arthurpass'


# Create a connection with the database service in local machine
con = pymysql.connect(host=host, port=port, user=user, passwd=password)

# Creating a cursor object
cursor = con.cursor()


# Use the realty schema
cursor.execute('''
    USE realty;
''')


# Convert the Dataframe into a list of arrays
sales_tuples = tuple(sales.to_records(index=False))

for data in range(len(sales_tuples)):
    
    # Create a new record
    query = "INSERT INTO sales (property_id, prop_type, prop_status, price, baths, beds, address_city, address_line, address_state_code, address_state, \
        address_county, addres_lat, address_lon, address_neighborhood_name) VALUES {}".format(sales_tuples[data])
    
    # Execute the query
    cursor.execute(query)


# Convert the Dataframe into a list of arrays
rents_tuples = tuple(rents.to_records(index=False))

for data in range(len(rents_tuples)):
    
    # Create a new record
    query = '''
        INSERT INTO rents (property_id, prop_type, prop_status, year_built, address_city, address_line, address_state_code, 
        address_state, address_county, address_lat, address_lon, address_neighborhood_name, community_price_max, community_price_min) 
        VALUES {}'''.format(rents_tuples[data])
    
    # Execute the query
    cursor.execute(query)


# Convert the Dataframe into a list of arrays
sold_tuples = tuple(sold.to_records(index=False))

for data in range(len(sold_tuples)):
    
    # Create a new record
    query = '''
        INSERT INTO sold (property_id, prop_type, prop_status, year_built, price, baths, beds, address_city, address_line, address_state_code, 
        address_state, address_county, address_lat, address_lon, address_neighborhood_name) 
        VALUES {}'''.format(sold_tuples[data])
    
    # Execute the query
    cursor.execute(query)


# Commit
con.commit()


con.close()


