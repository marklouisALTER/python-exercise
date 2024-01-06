import pandas as pd
import matplotlib.pyplot as plt
# Read the csv file and convert it to a DataFrame with separator of ,
data = pd.read_csv("tax_data_return.txt", sep=",");

# group the agi_stub and sum the N1 
counts = data.groupby("agi_stub").N1.sum()
# plot the count into bar
counts.plot.bar()
# show the plot
plt.show()
# print(data.head())