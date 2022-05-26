# %%
# Imports
import pandas as pd
import requests
import pymysql

# %%
# Set options
pd.options.display.max_rows = 100
pd.options.display.max_columns = 100

# %%
# Definition of function to get properties for sale
# "city":"New York City","state_code":"NY","limit":"5"
def get_sales(city, state_code, limit):
	url = "https://realty-in-us.p.rapidapi.com/properties/v2/list-for-sale"

	querystring = {"city":city,"state_code":state_code,"offset":"0","limit":limit,"sort":"relevance"}

	headers = {
		"X-RapidAPI-Host": "realty-in-us.p.rapidapi.com",
		"X-RapidAPI-Key": "80d4101192msha3850ddbf66ba87p1c5dc9jsn7ad589c1b934"
	}
	try:
		response_sale = pd.json_normalize(requests.request("GET", url, headers=headers, params=querystring).json(), record_path="properties", sep="_")
		return response_sale
	except:
		print("Error")

# %%
# Definition of function to get properties to rent
# "city":"New York City","state_code":"NY","limit":"5"
def get_rent(city, state_code, limit):
	url = "https://realty-in-us.p.rapidapi.com/properties/v2/list-for-rent"

	querystring = {"city":city,"state_code":state_code,"limit":limit,"offset":"0","sort":"relevance"}

	headers = {
		"X-RapidAPI-Host": "realty-in-us.p.rapidapi.com",
		"X-RapidAPI-Key": "80d4101192msha3850ddbf66ba87p1c5dc9jsn7ad589c1b934"
	}

	try:
		response_rent = pd.json_normalize(requests.request("GET", url, headers=headers, params=querystring).json(), record_path="properties", sep="_")
		return response_rent
	except:
		print("Error")

# %%
# Definition of function to get sold properties
# "limit":"200","city":"New York City","state_code":"NY"
def get_sold(city, state_code, limit):
	url = "https://realty-in-us.p.rapidapi.com/properties/v2/list-sold"

	querystring = {"offset":"0","limit":limit,"city":city,"state_code":state_code,"sort":"sold_date"}

	headers = {
		"X-RapidAPI-Host": "realty-in-us.p.rapidapi.com",
		"X-RapidAPI-Key": "80d4101192msha3850ddbf66ba87p1c5dc9jsn7ad589c1b934"
	}

	try:
		response_sold = pd.json_normalize(requests.request("GET", url, headers=headers, params=querystring).json(), record_path="properties", sep="_")
		return response_sold
	except:
		print("Error")

# %%
# Funtion to fill NAN values in the whole dataframe
def fill_na(df):
    columns = df.columns.to_list()
    for col in columns:
        if df[col].dtype == 'object':
            df[col].fillna("NA", inplace=True)
        elif df[col].dtype == 'int64':
            df[col].fillna(1, inplace=True)
        elif df[col].dtype == 'float64':
            df[col].fillna(1.0, inplace=True)
    return df

# %% [markdown]
# # Retrieving data

# %%
# List of relevant columns
sales_cols = ['property_id', 'prop_type', 'prop_status', 'price', 'baths', 'beds', 'address_city', 'address_line', 'address_state_code', \
    'address_state', 'address_county', 'address_lat', 'address_lon', 'address_neighborhood_name']

rents_cols = ['property_id', 'prop_type', 'prop_status', 'year_built', 'address_city', 'address_line', 'address_state_code', 'address_state', \
    'address_county', 'address_lat', 'address_lon', 'address_neighborhood_name', 'community_price_max', 'community_price_min']

sold_cols = ['property_id', 'prop_type', 'prop_status', 'year_built', 'price', 'baths', 'beds', 'address_city', 'address_line', 'address_state_code', \
    'address_state', 'address_county', 'address_lat', 'address_lon', 'address_neighborhood_name']

# %%
sales = get_sales("New York City", "NY", "200")
sales = sales[sales_cols]
sales.head()

# %% [markdown]
# 

# %%
rents = get_rent("New York City", "NY", "200")
rents = rents[rents_cols]
rents.head()


# %%
sold = get_sold("New York City", "NY", "200")
sold = sold[sold_cols]
sold.head()

# %%
# Remove NAN values from dataframes
sales = fill_na(sales)
rents = fill_na(rents)
sold = fill_na(sold)

# %%
# Check if there are NAN values
sales.isna().sum()

# %%
# For backup purpose, save dataframes into csv files
sales.to_csv("sales.csv", index=False)
rents.to_csv("rents.csv", index=False)
sold.to_csv("sold.csv", index=False)

# %%
# sales = pd.read_csv("sales.csv")
# rents = pd.read_csv("rents.csv")
# sold = pd.read_csv("sold.csv")

# %% [markdown]
# # Inserting data into MySQL

# %%
# Create a connection with the database service in local machine
con = pymysql.connect(host ='localhost', port=int(3306), user='arthur', passwd='123456')

# Creating a cursor object
cursor = con.cursor()

# %%
# Use the realty schema
cursor.execute('''
    USE realty;
''')

# %%
# Convert the Dataframe into a list of arrays
sales_tuples = tuple(sales.to_records(index=False))

for data in range(len(sales_tuples)):
    
    # Create a new record
    query = "INSERT INTO sales (property_id, prop_type, prop_status, price, baths, beds, address_city, address_line, address_state_code, address_state, \
        address_county, addres_lat, address_lon, address_neighborhood_name) VALUES {}".format(sales_tuples[data])
    
    # Execute the query
    cursor.execute(query)

# %%
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

# %%
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

# %%
# Commit
con.commit()

# %%
con.close()


