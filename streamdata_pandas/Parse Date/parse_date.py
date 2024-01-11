import pandas as pd


# survey_data = pd.read_excel("../Excel Sheet/fcc_servey.xlsx")
# print("survey_data.head())

# heres the raw data of the excel file 
# ---------------------------------------------------------------------
#    FreeCodeCamp New Developer Survey Responses, 2017        Unnamed: 1      Unnamed: 2  ...                              Unnamed: 95  Unnamed: 96     Unnamed: 97
# 0  Source: https://www.kaggle.com/fccuser/the-fre...               NaN             NaN  ...                                      NaN          NaN             NaN    
# 1                                                Age  AttendedBootcamp  BootcampFinish  ...                             SchoolDegree  SchoolMajor  StudentDebtOwe    
# 2                                                 27                 0             NaN  ...           some college credit, no degree          NaN             NaN    
# 3                                                 34                 0             NaN  ...           some college credit, no degree          NaN             NaN    
# 4                                                 21                 0             NaN  ...  high school diploma or equivalent (GED)          NaN             NaN    

# we choose the column that we want to show 
column_name = ["NetworkID", "Part1EndTime", "Part1StartTime", "Part2EndTime", "Part2StartTime"]

# we put sheet_name to specify what sheet in the excel file that we want to load
# we use skiprows = 2 to remove the upper row in the excel file the unnamed secion and the source link
# we use usecols to specify what column we want to show
survey_data = pd.read_excel("../Excel Sheet/fcc_servey.xlsx", sheet_name=1, skiprows=2, usecols=column_name)

# print the first 5 row of the survey data
print(survey_data.head())

# OUTPUT
#     NetworkID         Part1EndTime       Part1StartTime         Part2EndTime       Part2StartTime  StudentDebtOwe
# 0  6f1fbc6b2b  2017-03-09 00:36:22  2017-03-09 00:32:59  2017-03-09 00:59:46  2017-03-09 00:36:26             NaN
# 1  f8f8be6910  2017-03-09 00:37:07  2017-03-09 00:33:26  2017-03-09 00:38:59  2017-03-09 00:37:10             NaN
# 2  2ed189768e  2017-03-09 00:37:58  2017-03-09 00:33:53  2017-03-09 00:40:14  2017-03-09 00:38:02             NaN
# 3  dbdc0664d1  2017-03-09 00:40:13  2017-03-09 00:37:45  2017-03-09 00:42:26  2017-03-09 00:40:18             NaN
# 4  11b0f2d8a9  2017-03-09 00:42:45  2017-03-09 00:39:44  2017-03-09 00:45:42  2017-03-09 00:42:50             NaN

# NOW LETS PARSE THE DATE AND MERGE THE TWO COLUMN THEN VIEW THE SUMMARY
datetime_cols = {"Part1": ["Part1StartTime", "Part1EndTime"]}
# we combine the two column into one column 
date_sum = pd.read_excel("../Excel Sheet/fcc_servey.xlsx", sheet_name=1, skiprows=2, usecols=column_name, parse_dates=datetime_cols)

print(date_sum.head())
#                                      Part1   NetworkID         Part2EndTime       Part2StartTime  StudentDebtOwe
# 0  2017-03-09 00:32:59 2017-03-09 00:36:22  6f1fbc6b2b  2017-03-09 00:59:46  2017-03-09 00:36:26             NaN
# 1  2017-03-09 00:33:26 2017-03-09 00:37:07  f8f8be6910  2017-03-09 00:38:59  2017-03-09 00:37:10             NaN
# 2  2017-03-09 00:33:53 2017-03-09 00:37:58  2ed189768e  2017-03-09 00:40:14  2017-03-09 00:38:02             NaN
# 3  2017-03-09 00:37:45 2017-03-09 00:40:13  dbdc0664d1  2017-03-09 00:42:26  2017-03-09 00:40:18             NaN
# 4  2017-03-09 00:39:44 2017-03-09 00:42:45  11b0f2d8a9  2017-03-09 00:45:42  2017-03-09 00:42:50             NaN

# now if we put describe in here 
print(date_sum.head().describe())
#                                           Part1   NetworkID         Part2EndTime       Part2StartTime
# count                                         5           5                    5                    5
# unique                                        5           5                    5                    5
# top     2017-03-09 00:32:59 2017-03-09 00:36:22  6f1fbc6b2b  2017-03-09 00:59:46  2017-03-09 00:36:26
# freq                                          1           1                    1                    1

# lets look in the part 1 and set a format to follow all the data
date_sum["Part1"] = pd.to_datetime(date_sum["Part1"], format="%Y-%m-%d %H:%M:%S")

print(date_sum["Part1"].head())

