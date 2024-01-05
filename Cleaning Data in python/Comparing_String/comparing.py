from thefuzz import process
import pandas as pd

# Read the csv file and convert it to a DataFrame
restaurant = pd.read_csv('restaurants_dirty.csv')

# Fine the unique records in cusine_types
restaurant['type'].unique()
# print(restaurant.head())

# calculate all the similarity of types to all value of the types in restaurants
# print(process.extract('asian', restaurant['type'], limit = len(restaurant['type'])))
# print(process.extract('american', restaurant['type'], limit = len(restaurant['type'])))
# print(process.extract('italian', restaurant['type'], limit = len(restaurant['type'])))

# Some of the output its to loong
#('asian', 100, 26)
#  ||       ||  ||	
# the name, similarities, the index of the data
# [('asian', 100, 26), ('asian', 100, 65), ('asian', 100, 71), ('asian', 100, 79), ('indonesian', 80, 41) ....]

# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian', restaurant['type'], limit=len(restaurant.type))
# the . is same as the ['']

# Inspect the first 5 matches
print(matches[0:5])

# Iterate through the list of matches to italian
for match in matches:
  # Check whether the similarity score is greater than or equal to 80
  if match[1] >= 80:
    # Select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
    restaurant.loc[restaurant['type'] == match[0]] = 'italian'