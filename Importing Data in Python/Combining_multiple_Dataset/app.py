import pandas as pd

# note
# append() --> if we want to append rows to the end of a DataFrame, we can use the .append() method.
# ex: df1.append(df2)

# ignore_index to True -->> to renumber the rows so it will not repeat the two numbers like 0,0,1,1,2,2,3,3,4,4,5,5

# Example
# bookstores = firstsTwentyBookstore.append(nextTwentyBookstore, ignore_index=True)

# Combining the data row
# firstTwentyBookstore -->> first twentyrow
# nextTwentyBookstore -->> next second twetyrow that we want to merge in the firstTwentyBookstore
# set the ignore_index to True so it will not duplicate the index

# In terms of database we can use merge() method to combine the data

# Ex: merged = call_counts.merge(weather, left_on = "created_date",  right_on = "date")

# call_counts is first DataFrame
# weather is the second DataFrame that we want to merge in call_counts
# left_on --> is the column of the call_counts its the join key that we want to merge in
# ito yung key joins sa call count "created_date"
# right_on --> the column of the weather that has the join key that we want to merge in
# ito yung "date" na column ng weather sya yung key join nung sa kabila 


# Add an offset parameter to get cafes 51-100
# params = {"term": "cafe", 
#           "location": "NYC",
#           "sort_by": "rating", 
#           "limit": 50, -->> Limit of the rows
#           "offset" : 50} -->> We want to skip the first 50 rows

# result = requests.get(api_url, headers=headers, params=params)
# next_50_cafes = json_normalize(result.json()["businesses"])

# # Append the results, setting ignore_index to renumber rows
# cafes = top_50_cafes.append(next_50_cafes, ignore_index = True) -->> Append the next 50 and ignore_index true so it will renumber the rows

# # Print shape of cafes
# print(cafes.shape) -- cehck the row and column (100, 24) -->> (rows, columns)