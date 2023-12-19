from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine 
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Album', engine)

# Other way to print database
print(df.head())