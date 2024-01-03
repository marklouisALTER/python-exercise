import pandas as pd 

# import the file in csv using pandas dataframe
airlines = pd.read_csv('airlines_final.csv')

# find the dest_region and the dest_size in the file that contains unique values
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

'''
This is the output as you can see there is no format in capitalization in the dest_region and dest_size have whitespace characters

dest_region: the region
['Asia' 'Canada/Mexico' 'West US' 'East US' 'Midwest US' 'EAST US'
 'Middle East' 'Europe' 'eur' 'Central/South America'
 'Australia/New Zealand' 'middle east']

dest_size: the size of the destination
 ['Hub' 'Small' '    Hub' 'Medium' 'Large' 'Hub     ' '    Small'
 'Medium     ' '    Medium' 'Small     ' '    Large' 'Large     ']
'''
#THE SOLUTION 
# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower() 
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})

# Remove white spaces from `dest_size`
airlines['dest_size'] = airlines['dest_size'].str.strip()

# Verify changes have been effected
print(airlines['dest_region'])
print(airlines['dest_size'])
