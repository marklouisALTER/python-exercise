from sqlalchemy import create_engine, inspect
import pandas as pd
import matplotlib.pyplot as plt

engine = create_engine("sqlite:///data.sqlite");

query = """
SELECT *
FROM hpd311calls
WHERE complaint_type = 'SAFETY';
"""

inspector = inspect(engine)

table_names = inspector.get_table_names()

for table in table_names:
    print(table);

# safety_calls = pd.read_sql(query, engine)

# print(safety_calls.head())

# call_counts = safety_calls.groupby('borough').unique_key.count();
# call_counts.plot.barh();
# plt.show();


# Create query to get hpd311calls records about safety
# query = """
# SELECT *
# FROM hpd311calls
# WHERE complaint_type = 'SAFETY';
# """

# # Query the database and assign result to safety_calls
# safety_calls = pd.read_sql(query, engine)

# # Graph the number of safety calls by borough
# call_counts = safety_calls.groupby('borough').unique_key.count()
# call_counts.plot.barh()
# plt.show()

# Create query to get call counts by complaint_type
# query = """
# SELECT complaint_type, 
#      COUNT(*)
#   FROM hpd311calls
#   GROUP BY complaint_type;
# """

# # Create dataframe of call counts by issue
# calls_by_issue = pd.read_sql(query, engine)

# # Graph the number of calls for each housing issue
# calls_by_issue.plot.barh(x="complaint_type")
# plt.show()