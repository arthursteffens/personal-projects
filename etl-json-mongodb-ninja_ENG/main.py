import warnings
warnings.filterwarnings('ignore')

from functions import *

from glob import iglob
import pandas as pd
from pymongo import MongoClient
from sys import exit

# Fill with your MongoDB credentials
USER = 'root'
PASSWORD = 'rootpass'


# Connection to MongoDB
try:
    print("Connecting to MongoDB database...")
    client = MongoClient('localhost', 27017, username=USER, password=PASSWORD)
    print(f"Databases found: {client.list_database_names()}")
    print("OK.")
except Exception as e:
    print(f"Error connecting to database: {e}")
    exit("Exit without doing anything.")

# Create db and collection
db = client['ninja']
collection = db['johnny']

# Delete collection if exists
collection.drop()

# The sample folder contains 1% of the total files (about 256k).
# To use the full set, uncomment the line below and use json256k folder (unzip "json256k.7z")
#json_path = './json256k/'
json_path = './sample/'


# Function 'iglob' used to list and count json files in the directory
count_files = sum(1 for _ in iglob(json_path + "*.json"))
print(f"There are {count_files} files in {json_path} directory.")

# If the full set of json files is used, this function takes about 3h to run
print("Generating dataframe from json files... (this may take awhile)")
df = gen_dataframe(count_files, json_path)
print("OK.")

print("Saving dataframe into csv files...")
df.to_csv("./df.csv", index=None)
print("OK.")


# Read the csv and transform it to dict.

# For practical purposes, the csv with full set of files is already on the directory.
# Uncomment the line below to use the full dataset and comment the line that reads df.csv
#df = pd.read_csv("./full_df/full_df.csv")
df = pd.read_csv("./df.csv")
df_dict = df.to_dict('records')

# Check the number of records in dataframe
print(f"Checking records of dataframe: \n {df.count()}")

# Insert data into MongoDB "johnny" collection
print("Inserting data into MongoDB...")
insert_into_mongo(collection, df_dict)
print("OK.")

# Close DB connection
print("Closing database connection and quitting program.")
client.close()