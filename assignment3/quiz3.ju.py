# %%
import numpy as np
import pandas as pd

# %%
student = {
    "Name": ["James", "Mike", "Sally"],
    "School": ["Business", "Law", "Engineering"],
}


student_df = pd.DataFrame(student).set_index("Name")

staff = {
    "Name": ["Kelly", "Sally", "James"],
    "Role": ["Director of HR", "Course liasion", "Grader"],
}

staff_df = pd.DataFrame(staff).set_index("Name")
# %%
pd.merge(student_df, staff_df, how='left', left_index=True, right_index=True)
# pd.merge(student_df, staff_df, how='right', left_index=True, right_index=True)
# pd.merge(staff_df, student_df, how="right", left_index=False, right_index=True)
# If both have same index, it needs to
# pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)

# %%
# Q2
data = {
    "Serial No.": [1, 2, 3, 4, 5],
    "gre score": [337, 324, 316, 322, 314],
    "toefl score": [118, 107, 104, 110, 103],
}

df = pd.DataFrame(data).set_index("Serial No.")
frames = ["gre score", "toefl score"]
df["AVG"] = df[frames].apply(lambda z: np.mean(z), axis=1)
result_df = df.drop(frames, axis=1)
result_df

# df['AVG']
# frames = ['P2010', 'P2011', 'P2012', 'P2013','P2014', 'P2015']
# df['AVG'] = df[frames].apply(lambda z: np.mean(z), axis=x)
# result_df = df.drop(frames,axis=y)
# %%
# Q3
import pandas as pd

df = pd.DataFrame(
    ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D"],
    index=[
        "excellent",
        "excellent",
        "excellent",
        "good",
        "good",
        "good",
        "ok",
        "ok",
        "ok",
        "poor",
        "poor",
    ],
    columns=["Grades"],
)
df
# %%
my_categories = pd.CategoricalDtype(
    categories=["D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"],
    ordered=True,
)
# %%
grades = df["Grades"].astype(my_categories)
result = grades[(grades > "B") & (grades < "A")]
result

# %%
# Q4
data = {
    "world rank": [1, 2, 3, 4, 5],
    "institution": ["Harvard", "Massachusetts", "Stanford", "Cambridge", "California"],
    "country": ["USA", "USA", "USA", "United Kingdom", "USA"],
    "Rank_Level": [
        "First Tier Top University",
        "First Tier Top University",
        "First Tier Top University",
        "First Tier Top University",
        "First Tier Top University"
    ],
}

df = pd.DataFrame(data)
# %%
data = {
    'Year': ['2019', '2019', '2019', '2020', '2020', '2020'],
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q1', 'Q2', 'Q3'],
    'Sales': [100, 200, 150, 250, 300, 200]
}

# create DataFrame from data
df = pd.DataFrame(data)
df

# %%
# create pivot table
pivot_table = pd.pivot_table(df, values='Sales', index='Quarter', columns='Year', aggfunc='sum', margins=True)
pivot_table

# %%
# Q5
import pandas as pd
(pd.Timestamp('11/29/2019') + pd.offsets.MonthEnd()).weekday()
# pd.offsets.MonthEnd()
# pd.Timestamp('11/29/2019').weekday()
pd.Timestamp('11/29/2019') + pd.offsets.MonthEnd()

# %%
# Q6
filling_mean = lambda g: g.fillna(g.mean())
# df.groupby(group_key).transform(filling_mean)
# df.groupby(group_key).apply(filling_mean)
# df.groupby(group_key).aggregate(filling_mean)
# df.groupby(group_key).filling_mean()

# %%
# Q7
student = {
    "First Name": ["James", "Mike", "Sally"],
    "Last Name": ["Hammond", "Smith", "Brooks"],
    "School": ["Business", "Law", "Engineering"],
}

student_df = pd.DataFrame(student)

staff = {
    "First Name": ["Kelly", "Sally", "James"],
    "Last Name": ["Desjardins", "Brooks", "Wide"],
    "Role": ["Director of HR", "Course liasion", "Grader"],
}

staff_df = pd.DataFrame(staff)

# %%
pd.merge(staff_df, student_df, how='right', on=['First Name', 'Last Name'])
# pd.merge(student_df, staff_df, how='inner', on=['First Name', 'Last Name'])
# pd.merge(student_df, staff_df, how='right', on=['First Name', 'Last Name'])
# pd.merge(staff_df, student_df, how='outer', on=['First Name', 'Last Name'])

# %%
# Q9
pd.Period('01/12/2019', 'M') + 5

# %%
# Q10
fruit = {
    "": ["apple", "mango", "potato", "onion", "brocolli"],
    "class": ["fruit", "fruit", "vegetable", "vegetable", "vegetable"],
    "avg calories per unit": [95, 202, 164, np.nan, 207],
}

fruit_df = pd.DataFrame(fruit)
df = fruit_df

# %%
# df.groupby('class', axis = 0)
# grouped = df.groupby(['class', 'avg calories per unit'])
# df.groupby('class')
# df.groupby('vegetable')
