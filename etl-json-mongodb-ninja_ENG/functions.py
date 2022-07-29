import pandas as pd
import json

# Function to read json file
def read_json(file_json):
    with open(file_json, 'r') as f:
        return json.load(f)

# Generates a pandas dataframe with data from json files
def gen_dataframe(count_files, json_path):
    df_data = pd.DataFrame()
    for i in range(count_files):
        df = pd.DataFrame(read_json(f"{json_path}{str(i+1)}.json"))
        df['Name'] = f"Johnny #{str(i+1).zfill(6)}"
        df['Background'] = df['attributes'][0]['value']
        df['Legs'] = df['attributes'][1]['value']
        df['Body'] = df['attributes'][2]['value']
        df['Eyes'] = df['attributes'][3]['value']
        df['Head'] = df['attributes'][4]['value']
        df['Arms'] = df['attributes'][5]['value']
        df['Pets'] = df['attributes'][6]['value']
        df.drop(['attributes', 'dna', 'edition'], axis=1, inplace=True)
        df.drop_duplicates(inplace=True)
        df_data = df_data.append(df)
    return df_data

# Insert each line of data frame into a document inside MongoDB collection
def insert_into_mongo(collection, df_dict):
    for item in df_dict:
        collection.insert_one(item)