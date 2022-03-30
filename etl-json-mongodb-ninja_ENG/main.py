# Packages used on this script

from json import load
from json import dump
from glob import iglob
from os import listdir
from os import path
from pymongo import MongoClient


# Function to read json file

def read_json(file_json):
    with open(file_json, 'r') as f:
        return json.load(f)


# Connection to MongoDB

client = MongoClient('localhost', 27017)
db = client['ninja']
collection = db['johnny']


# Create a list with each file in the "jsonPath" directory
jsonPath = './json256k/'
file = os.listdir(jsonPath)


# Function 'iglob' used to list and count json files in the directory

countFiles = sum(1 for i in iglob(jsonPath + "*.json"))
print("There are {} files in {} directory.".format(countFiles, jsonPath))


# Modify the shape of json files easier reading and modeling in the database 

for i in range(countFiles):
    file_json = jsonPath + file[i]
    
    if os.path.exists(file_json):
        data = read_json(file_json)
        
        name = "Johnny #"+ str(i+1).zfill(6)
        
        # Create a dictionary
        dict = {
            "name": name,
            }
        
        # Populate dictionary with json data
        for j in range(7):
            tt = data["attributes"][j]["trait_type"]
            value = data["attributes"][j]["value"]
            dict[tt] = value
        
        # Save json file with modified information
        with open(file_json, "w") as outfile:
            json.dump(dict, outfile)
            print("File {} modified".format(file[i]))
                  
    else:
        print("No more files")
        continue



# Insert modified file into MongodB 'johnny' collection

for i in range(countFiles):
    file_json = jsonPath + file[i]
    file_data = read_json(file_json)
    collection.insert_one(file_data)
    print("File {} loaded".format(str(i+1)))


# Close DB connection
client.close()
