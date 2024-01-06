import pandas as pd

# create a column list that you want to show
cols = ['zipcode', 'agi_stub', 'mars1', 'MARS2', 'NUMDEP']
# import the file using read_csv in pandas library and usecols to get the cols that you want 
# nrows to filter the rows that we what
# skiprows is to filter first 500 rows
# header = none is required for the header column to be none to know that there is no header
data = pd.read_csv('tax_data_return.txt', nrows=500, skiprows = 500, header=None);