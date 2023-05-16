# %%
# Q1
import pandas as pd

sdata = {"Ohio": 35000, "Texas": 71000, "Oregon": 16000, "Utah": 5000}
obj1 = pd.Series(sdata)
states = ["California", "Ohio", "Oregon", "Texas"]
obj2 = pd.Series(sdata, index=states)
obj3 = pd.isnull(obj2)

# %%
x = obj2["California"]
obj2["California"] != x

# %%
import math

math.isnan(obj2["California"])

# %%
obj3["California"]

# %%
obj2["California"] == None

# %%
# Q2
import pandas as pd

d = {"1": "Alice", "2": "Bob", "3": "Rita", "4": "Molly", "5": "Ryan"}
S = pd.Series(d)

# %%
# print(S.loc[0:2])
# print(S.loc[0:3])
# print(S.iloc[0:2])
print(S.iloc[0:3])

# %%
# Q3
data = {
    "Name": ["John", "Emily", "Kate", "Alex"],
    "Age": [28, 25, 31, 22],
    "Gender": ["M", "F", "F", "M"],
    "Salary": [50000, 60000, 70000, 45000],
}

df = pd.DataFrame(data)
# df = df.rename(mapper = lambda x: x.upper(), axis = 1)
# df.rename(mapper = lambda x: x.upper(), axis = 1, inplace = True)
# df = df.rename(mapper = lambda x: x.upper(), axis = 'columns')
df.rename(mapper=lambda x: x.upper(), axis=1)
df

# %%
# Q4
data = {
    "Serial No.": [1, 2, 3, 4, 5],
    "gre score": [337, 324, 316, 322, 314],
    "toefl score": [118, 107, 104, 110, 103],
}

df = pd.DataFrame(data).set_index("Serial No.")

# df[df['toefl score'] > 105]
df.where(df["toefl score"] > 105)
# df.where(df['toefl score'] > 105).dropna()

# %%
# Q6
data = {
    "": ["Ohio", "Colorado", "Utah", "New York"],
    "one": [0, 4, 8, 12],
    "two": [1, 5, 9, 13],
    "three": [2, 6, 10, 14],
    "four": [3, 7, 11, 15],
}

df = pd.DataFrame(data).set_index("")

# df.drop('one', axis = 1)
df.drop("two")
# df.drop(['Utah', 'Colorado'])
# df.drop('Ohio')

# %%
# Q7
import pandas as pd

s1 = pd.Series({1: "Alice", 2: "Jack", 3: "Molly"})
s2 = pd.Series({"Alice": 1, "Jack": 2, "Molly": 3})

# print(s2[1])
print(s2.iloc[1])
# print(s2.loc[1])
print(s1.loc[1])

# %%
# Q8
# s1.append(s2)
for i in s1.iteritems():
    print(i)

# %%
# Q9
data = {
    "Serial No.": [1, 2, 3, 4, 5],
    "gre score": [337, 324, 316, 322, 314],
    "toefl score": [118, 107, 104, 110, 103],
}

df = pd.DataFrame(data).set_index("Serial No.")

print((df["toefl score"] > 105) & (df["toefl score"] < 115))
# print(df[(df['toefl score'].isin(range(106, 115)))])
# print(df[(df['toefl score'] > 105) & (df['toefl score'] < 115)])
# print(df[df['toefl score'].gt(105) & df['toefl score'].lt(115)])

# %%
# Q10
data = {
    "(Major)": ["Mathematics", "Sociology"],
    "Name": ["Alice", "Jack"],
    "Age": [20, 22],
    "Gender": ["F", "M"],
}

df = pd.DataFrame(data).set_index("(Major)")

# print(df["Mathematics"])
print(df.T["Mathematics"])
# print(df["Alice"])
# print(df.iloc["Mathematics"])
