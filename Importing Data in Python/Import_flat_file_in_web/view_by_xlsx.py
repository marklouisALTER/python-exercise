import pandas as pd

#### note you need to install xlrd to read xls files

# get the link of excel
url = 'https://assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# read the excel file
xls = pd.read_excel(url, sheet_name=None)

# print the sheet name shell
print(xls.keys())
# there are two sheet name in this xls the one is 1700 and 1900

#lets print a sheet name head
print(xls['1900'].head())