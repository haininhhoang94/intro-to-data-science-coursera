# import library
import re

# Let's do a basic search
text = "This is a good day."

# if re.search("good", text):
#    print("Wonderful!")
# else:
#    print("Alas: ()")

# Let's do another search
# findall
text = "Amy works diligently. Amy gets good grades. Our student Amy is sucessful"

re.findall("Amy", text)

# let's do search regex with ^, $
# => ^ is the pattern need to start with ...
# => $ is the pattern need to end with ...
text = "Amy works diligently. Amy gets good grades. Our student Amy is sucessful"

re.search("^Amy", text)

# re.search("$Amy", text)
re.findall("$Amy", text)

# Pattern and Character Classes
grades = "ACAAAABCBCBAA"

# findall
re.findall("B", grades)

# finding all the pattern with either A or B
re.findall("[AB]", grades)

# finding all the pattern with a range
# in this case, we find a pattern that has A follow with either B or C
re.findall("[A][B-C]", grades)

# finding all the pattern with a range
# in this case, we find a pattern that has A follow with either B or C
# alternative way for above command
re.findall("AB|AC", grades)

# finding all the grades which are not A. Note: the [] is the
# negate statement, that mean a FALSE statement
re.findall("[^A]", grades)

# match any value at the beginning of the string which is not an A
re.findall("^[^A]", grades)

# Quantifiers
# How many times has this student been on a back-to-back A's streak?
# e{m,n} - m is the min number want to match
# n is the max number
re.findall("A{2,10}", grades)

# If single value, it is both m and n
re.findall("A{2}", grades)

# Find a decreasing trend in a student grades. In this case, we find a
# straight A following by B and C
re.findall("A{1,10}B{1,10}C{1,10}", grades)

# Let's import a file in wikipedia description
with open("./data/ferpa.txt", "r") as file:
    wiki = file.read()
# and test the printout

# Finding all the segments that contain the [edit]
# note the escapee \
# in this case, we find until its reach the limit of 100
re.findall("[a-zA-Z]{1,100}\[edit\]", wiki)

# Alternative way -> \w to match any letters include digits and numbers
re.findall("[\w]{1,100}\[edit\]", wiki)

# Alternative way -> use * to find all instead of limit to 100
re.findall("[\w]*\[edit\]", wiki)

for title in re.findall("[\w]*\[edit\]", wiki):
    # Just for taking the first result
    print(re.split("[\[]", title)[0])
    # FIX:


# Group
re.findall("([\w]*)(\[edit\])", wiki)


for item in re.finditer("([(\w)]*)(\[edit\])", wiki):
    print(item.groups())


for item in re.finditer("([(\w)]*)(\[edit\])", wiki):
    print(item.group(1))
