import pandas as pd

# import the excel file and select the sheetname through its label which is '2017' or its index within the excel file which is 1
# the index of the 2017 sheet is 1 before 2016 which is 0
survey_data_2017 = pd.read_excel('fcc_servey', sheet_name='2017')
surver_data_indexOne = pd.read_excel('fcc_survey', sheet_name=1)
# let check if 2017 is in index 1 
print(survey_data_2017.equals(surver_data_indexOne)) # True