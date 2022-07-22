import requests
import pandas as pd

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
	except Exception as e:
		print(f"Error: {e}")


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