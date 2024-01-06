import pandas as pd

data = pd.read_csv("tax_data_return.txt", usecols=['zipcode', 'agi_stub', 'STATEFIPS']);

print(data.dtypes)
# output
# STATEFIPS     int64
# STATE        object
# zipcode       int64 ---- LETs change this into object with is string in python 
# agi_stub      int64
# N1            int64
#               ...
# A85300        int64
# N11901        int64
# A11901        int64
# N11902        int64
# A11902        int64

dataFixed = pd.read_csv("tax_data_return.txt", dtype={"zipcode": str })
print(dataFixed.dtypes)

#output 
# STATEFIPS     int64
# STATE        object
# zipcode      object --- now we change the int64 into string(object)
# agi_stub      int64
# N1            int64
#               ...
# A85300        int64
# N11901        int64
# A11901        int64
# N11902        int64
# A11902        int64
# Length: 147, dtype: object

# So if you want to filter the 0 in the columns like this one 
print(data.head(5))
# Length: 147, dtype: object
#    STATEFIPS  zipcode  agi_stub
# 0         50        0         1
# 1         50        0         2
# 2         50        0         3
# 3         50        0         4
# 4         50        0         5

# we can you this to view all the 0 zipcode in the rows this is the first approach
filterZero = pd.read_csv("tax_data_return.txt", usecols=['zipcode', 'agi_stub', 'STATEFIPS'], na_values={"zipcode": 0})

# second approach
null_values = {"zipcode": 0}
filterZero = pd.read_csv("tax_data_return.txt", usecols=['zipcode', 'agi_stub', 'STATEFIPS'], na_values=null_values)

# two are same its just where you are comfortable to used them

# it will return the boolean value of the zipcode that is 0
print(filterZero.zipcode.isna())

# IF YOU ENCOUNTER ERROR TO PRINT THE DATA ROWS WE CAN USE THIS
# SET error_bad_lines = False so it will continue to read the data until the end of the file it will skip the error 
# Error row instead of throwinge rror 
# warned_bad_lines --- this will tell if there is unparsable data in the file 

# it will ignore if there is unparsable row and throw an warning if there is 
filterZero = pd.read_csv("tax_data_return.txt", error_bad_lines = False, warned_bad_lines= True);

try:
  # Set warn_bad_lines to issue warnings about bad records
  data = pd.read_csv("tax_data_return.txt", error_bad_lines=False, warn_bad_lines=True)
  
  # View first 5 records
  print(data.head())
  
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")
