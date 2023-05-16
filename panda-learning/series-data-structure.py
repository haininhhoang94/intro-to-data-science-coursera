##
import pandas as pd
import numpy as np

##
students = ["Alice", "Jack", "Molly"]
pd.Series(students)

##
numbers = [1, 2, 3]
pd.Series(numbers)

##
# test how Pandas handle missing data
students = ["Alice", "Jack", None]
pd.Series(students)
# it is being converted to object

##
numbers = [1, 2, None]
pd.Series(numbers)
# it is converted to NaN with float64

##
# NaN is not equal to None
np.nan == np.nan

##
np.isnan(np.nan)

##
# pandas with dictionary
students_classes = {"Alice": "Physics", "Jack": "Chemistry", "Molly": "English"}
s = pd.Series(students_classes)
s

##
s.index

##
# dtype object can store everything
students = [("Alice", "Physics"), ("Jack", "Chemistry"), ("Molly", "English")]
pd.Series(students)

##
students_classes = {"Alice": "Physics", "Jack": "Chemistry", "Molly": "English"}
s = pd.Series(students_classes, index=["Alice", "Molly", "Sam"])
s
# Sam is NaN because no value

# Querying series

##
students_classes = {
    "Alice": "Physics",
    "Jack": "Chemistry",
    "Molly": "English",
    "Sam": "History",
}
s = pd.Series(students_classes)
s

##
s.iloc[3]

##
s.loc["Molly"]
# Note: loc and iloc is attribute, not function/method that's why it uses
# []

##
s[3]

##
s["Molly"]

##
class_code = {99: "Physics", 100: "Chemistry", 101: "English", 102: "History"}
s = pd.Series(class_code)

##
s[0]  # error

##
# Example for function (draft idea)
grades = pd.Series([90, 80, 70, 60])

total = 0
for grade in grades:
    total += grade
print(total / len(grades))

##
# Vectorization
print(np.sum(grades) / len(grades))

##
numbers = pd.Series(np.random.randint(0, 1000, 10000))
numbers.head()

##
len(numbers)

##
%%timeit -n 100
total = 0
for grade in grades:
    total += grade
print(total / len(grades))

##
%%timeit -n 100
print(np.sum(grades) / len(grades))

##
numbers.head()

##
%%timeit -n 100
# Broastcast
numbers = pd.Series(np.random.randint(0, 1000, 10000))
numbers+=2
numbers.head()

##
%%timeit -n 100
numbers = pd.Series(np.random.randint(0, 1000, 10000))
# iteration way
for label, value in numbers.iteritems():
    numbers.at[label] = value+2
numbers.head()

##
# Append
all_students_classes = pd.Series(students_classes).append(pd.Series(students_classes))
all_students_classes
