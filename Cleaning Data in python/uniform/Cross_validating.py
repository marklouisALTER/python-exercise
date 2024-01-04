# NOTE -
# Cross validation is done if the data came from a different source and we want to check the data is correct or not
import pandas as pd 
import datetime as dt

banking = pd.read_csv('banking_dirty.csv')

# Lets print first the data that were going to validate
print(banking.head())

#create a column list for the label columms to sum it later
fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']

# Find the rows where the fund_columns row sum == inv_amount
inv_equ = banking[fund_columns].sum(axis = 1) == banking['inv_amount']

# Store consistent and inconsistent data
consistent_data = banking[inv_equ]
inconsistent_data = banking[~inv_equ]

# you can use thus ~ to see the inconsistent data

# print the inconsistent data
print("Number of inconsistent investment data :", inconsistent_data.shape[0])

# the output is 8 which means there are 8 inconsistent data
# Number of inconsistent investment data : 8

# BONUS
# It will check if there is na/ NaN . or missing data in columns with summary accross the data
print(banking.isna().sum())

# WE CAN VIEW IT by describe to see the summary of the data like : 
# create a value of missing
inconsistent_data = banking.isna()
print(inconsistent_data.describe())