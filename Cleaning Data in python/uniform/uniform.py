import pandas as pd
import datetime as dt

# import the data
banking = pd.read_csv('banking_dirty.csv');

# print the first 5 row because the fdefault value of head is 5 if there is no value
print(banking['account_opened'].head())

#convert all the date into same format and if there is any error then replace it with NaT
banking['account_opened'] = pd.to_datetime(banking['account_opened'], infer_datetime_format = True, error = 'coerce')

# Get year of account opened
banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')

# Print acct_year
print(banking['acct_year'])