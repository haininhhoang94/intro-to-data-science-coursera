# %%
from math import nan
import pandas as pd
import numpy as np

# %%
# Q1
a = np.arange(8)
b = a[4:6]
b[:] = 40
c = a[4] + a[6]
c
# %%
# Q2
import re

s = "ABCAC"
A = re.match("A", s) == True
# B = len(re.search('A', s)) == 2
C = len(re.split("A", s)) == 2
D = bool(re.match("A", s)) == True
print(A)
print(C)
print(D)


# %%
# Q3
def result():
    s = "ACAABAACAAABACDBADDDFSDDDFFSSSASDAFAAACBAAAFASD"

    result = []
    # compete the pattern below
    # pattern = "[AAA][a-z]+"
    # NOTE: positive look behind
    pattern = "(?<=AAA).*?(?=AAA|$)"
    for item in re.finditer(pattern, s):
        # identify the group number below.
        result.append(item.group())

    return result


result()
# %%
# FIX: this question is very weird lol. the 2d series does not creatable at the moment
# Q4
col1 = ["d", "b", "a", "c"]
col2 = [4, 7, -5, 3]

df = pd.Series(col2, index=col1)

print(df[0])
print(df["d"])
print(df.index[0])
print(df.iloc[0])

# %%
# Q5
data = [20, 15, 18, 31]
index = ["Mango", "Strawberry", "Blueberry", "Vanilla"]
s1 = pd.Series(data, index=index)

data = [20, 30, 15, 20, 20]
index = ["Strawberry", "Vanilla", "Banana", "Mango", "Plain"]
s2 = pd.Series(data, index=index)

s3 = s1.add(s2)

print(s3["Blueberry"] == s1.add(s2, fill_value=0)["Blueberry"])
print(s3["Blueberry"] == s1["Blueberry"])
print(s3["Mango"] >= s1.add(s2, fill_value=0)["Mango"])
print(s3["Plain"] >= s3["Mango"])

# %%
# Q6
df = pd.DataFrame(
    {
        "Name": ["Tom", "Jack", "Emma", "Alex"],
        "Age": [25, 28, 21, 32],
        "City": ["New York", "San Francisco", "Boston", "Chicago"],
    }
)
df.set_index("Name")
df.set_index("Name").reset_index()
df
# %%
# Q7
S = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])

print(S["b":"e"])
print(S[["b", "c", "d"]])
print(S[S <= 3][S > 0])
print(S[1:4])
# %%
# Q8
df = pd.DataFrame(
    {
        "": ["R1", "R2", "R3", "R4"],
        "a": [5, 5, 71, 67],
        "b": [6, 82, 31, 37],
        "c": [20, 28, 92, 49],
    }
).set_index("")

f = lambda x: x.max() + x.min()
df_new = df.apply(f)

df_new[1]
# %%
# Q9
index = ["Argentina", "Australia", "Austria", "Belgium", "Brazil"]
col1 = [np.NaN, 47.9425, np.NaN, 51.8750, np.NaN]
col2 = [44.1, 44.2, 44.3, 44.4, 44.5]
col3 = [np.NaN, 49.2, np.NaN, 49.08, 49.56]
col4 = [np.NaN, 47.28, 47.07, 46.7, np.NaN]
col5 = [44.7, 45.8, 45.1, 47.0, 44.78]

columns = pd.MultiIndex.from_product(
    [
        ["mean", "amax"],
        [
            "First Tier Top University",
            "Other Top University",
            "Second Tier Top University",
            "Third Tier Top University",
            "All",
        ],
    ]
)

df = pd.DataFrame(
    np.array([col1, col2, col3, col4, col5, col1, col2, col3, col4, col5]).transpose(),
    columns=columns,
    index=index,
)

# df.stack()
# df.unstack()
# df.stack().stack()
df.unstack().unstack()

# %%
# Q10
cols = ["Item", "Store", "Quantity sold"]
col1 = ["item_1", "item_1", "item_1", "item_2", "item_2", "item_2"]
col2 = ["A", "B", "C", "A", "B", "C"]
col3 = [10.0, 20.0, np.nan, 5.0, 10.0, 15.0]

df = pd.DataFrame(np.array([col1, col2, col3]).transpose(), columns=cols)

df.groupby('Item').sum()#.iloc[0]['Quantity sold']
