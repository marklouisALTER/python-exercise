import pandas as pd

# import the excel file and select the sheetname through its label which is '2017' or its index within the excel file which is 1
# the index of the 2017 sheet is 1 before 2016 which is 0
survey_data_2017 = pd.read_excel('fcc_servey', sheet_name='2017')
surver_data_indexOne = pd.read_excel('fcc_survey', sheet_name=1)
# let check if 2017 is in index 1 
print(survey_data_2017.equals(surver_data_indexOne)) # True

# if we want to view all the sheetname all in once we can just do this "sheet_name = None"
survey_data_all = pd.read_excel('fcc_survey', sheet_name=None)
print(type(survey_data_all)) # if we print the type of the survey data the output is "OrderedDict" and inside that is the 
# DataFrame of two sheetname which is 2016 and 2017

# So if you want to change the value of the data into bool 
# we can do this
survey_data_all = pd.read_excel('fcc_survey', 
                                sheet_name=None,
                                dtype={"column_name": bool}, # so the column name is str to bool
                                # but there is prob because bool is true or false and the value of your column_name is 
                                # let say "Yes" or "No" so we need to change the value of the column_name into bool
                                # were going to pass new arguments
                                true_values=['Yes'], # so it will enterpret that "Yes" is TRUE
                                false_values=['No'], # so it will enterpret that "No" is FALSE
                                )

print(survey_data_all.sum())
# it will print all the data that have a value as true like +1 if false or no value 0