##
# import
import pandas as pd

##
record1 = pd.Series({"Name": "Alice", "Class": "Physics", "Score": 85})
record2 = pd.Series({"Name": "Jack", "Class": "Chemistry", "Score": 82})
record3 = pd.Series({"Name": "Helen", "Class": "Biology", "Score": 90})

##
df = pd.DataFrame([record1, record2, record3], index=["school1", "school2", "school1"])
df.head()

##
df.loc["school2"]

##
type(df.loc["school2"])

##
df.loc["school1"]

##
type(df.loc["school1"])

##
df.loc["school1", "Name"]

##
# Transpose
df.T

##
# Call loc on transpose
df.T.loc["Name"]

##
df.loc["school1"]["Name"]

##
print(type(df.loc["school1"]))
print(type(df.loc["school1"]["Name"]))

##
# how to use : operator
df.loc[:, ["Name", "Score"]]

##
df.drop("school1")

##
# the data still intact because of no inplace=True
df

##
copy_df = df.copy()
copy_df.drop("Name", inplace=True, axis=1)
copy_df

##
# Alternative way
del copy_df['Class']
copy_df

##
df['DataRanking'] = None
df
