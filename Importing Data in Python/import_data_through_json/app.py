import pandas as pd 
import matplotlib.pyplot as plt
#  Create dataframe from json file
df = pd.read_json("dhs_daily_report.json")

# we are converting the date_of_census column to datetime
df['date_of_census'] = pd.to_datetime(df['date_of_census'])

# We are plotting the total_adults_in_shelter column
df.plot(x="date_of_census", y="total_adults_in_shelter")

# And we're going to show the plt
plt.show()

# Print the head of df
# print(df.describe())