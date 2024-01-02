#Converting avg_rating > 5  to 5
movies.loc[movies['avg_rating'] > 5, 'avg_rating'] = 5

# if you want to check if its true
assert movies['avg_rating'].max() <= 5
# if no output it means its passed

# to check what types of the data is 
#  import nesessary library 
# you can use .dtypes to check the data types
user_types.dtypes

# like for example the date type is object and you want to convert it into date
user_signups['subscription_date'] = pd.to_datetime(user_signups['subscription_date']).dt.date

# -------- Another Example ---------#
# ----------------------------------#
# Path: Cleaning%20Data%20in%20python/numeric_data.py

# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print tire size description
print(ride_sharing['tire_sizes'].dtype)

# -------- Another Example ---------#
# ----------------------------------#

# Convert ride_date to date
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date

# Save today's date
today = dt.date.today();

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())
