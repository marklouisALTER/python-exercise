from urllib.request import urlretrieve
import pandas as pd
import matplotlib.pyplot as plt
#sample flat file of datacamp
url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv';

#save the file locally
# urlretrieve(url, 'winequality-red.csv');

# view the flat file
# the sep is seperator we usually also use the delimiter like tab and comma
df = pd.read_csv(url, sep=';');

# we access the df by using iloc so what is icloc?
# iloc is accessing your data trough indexing the arguments in iloc is 
# [row, column] so if you want to access the first row and first column
# this : is to access all the row and the second is access the first column.
# the hist() function is to plot the histogram of the data
df.iloc[:, 0].hist();
# the xlabel is the label of x in the histogram
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)');
# the ylabel is the label of y in the histogram
plt.ylabel('count')
# we need to put .show() to view the hist() function
plt.show()

# print the head of the dataframe
print(df.head());