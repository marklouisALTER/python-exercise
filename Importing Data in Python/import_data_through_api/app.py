import pandas as pd
import requests

api_url = 'https://api.yelp.com/v3/businesses/search'

parameters = {"term": "cafe",
                "location": "NYC"}
# Get data about NYC cafes from the Yelp API
headers = {"Authorization": "Bearer {}".format(api_key)}

data = requests.get(api_url, headers=headers, params=parameters)

# turn the data into JSON format
data_json = data.json()

# Load the data into DataFrame
cafes = pd.DataFrame(data['businesses'])

# view the data's dtypes
print(cafes.dtypes)


## IMPORTING DATA WITH NESTED JSON 
# Load json_normalize()
from pandas.io.json import json_normalize

# Isolate the JSON data from the API response
data = data.json()

# Flatten business data into a dataframe, replace separator
cafes = json_normalize(data["businesses"],
                       sep="_")

# View data
print(cafes.head())

# Load other business attributes and set meta prefix
# flat_cafes = json_normalize(data["businesses"],
#                             sep="_",
#                     		record_path="categories", -->> we specify the column we want to flatten
#                     		meta=["name",  -->> meta is we specify or select the column we want to flatten
#                                   "alias",  
#                                   "rating",
#                           		  ["coordinates", "latitude"], 
#                           		  ["coordinates", "longitude"]],
#                     		meta_prefix="biz_") -->>  to avoid duplication of the column names