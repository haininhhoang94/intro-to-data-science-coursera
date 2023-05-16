# https://www.coursera.org/learn/python-data-analysis/programming/4Wy6F/assignment-1/lab?path=%2Fnotebooks%2Fassignments%2Fassignment1%2Fassignment1.ipynb
# %%
import re


# %%
def example_word_count():
    # This example question requires counting words in the example_string below.
    example_string = "Amy is 5 years old"

    # YOUR CODE HERE.
    # You should write your solution here, and return your result, you can comment out
    # or delete the
    # NotImplementedError below.
    result = example_string.split(" ")
    return len(result)

    # raise NotImplementedError()


# %%
example_word_count()


# %%
# Part A
# Find a list of all of the names in the following string using regex
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    result = re.findall("[A-Z][\w]*[\s,]", simple_string)
    result = [e.replace(",", "") for e in result]
    return result
    # raise NotImplementedError()


# %%
names()



# %% [markdown]
# Part B
The dataset file in assets/grades.txt contains a line separated list
of people with their grade in a class. Create a regex to generate
a list of just those students who received a B in the course
# %%
def grades():
    with open("./data/grades.txt", "r") as file:
        grades = file.read()

    result = []
    cache = re.findall("[\w]*\s[\w]*:[\s]B", grades)
    for element in cache:
        element = re.split("[:]", element)[0]
        result.append(element)
    return result
    # raise NotImplementedError()


# %%
grades()
# len(grades())


# %%
# Part C
# Convert the logfile into list of dictionary
# example_dict = {"host":"146.204.224.152",
# "user_name":"feest6811",
# "time":"21/Jun/2019:15:45:24 -0700",
# "request":"POST /incentivize HTTP/1.1"}
def logs():
    with open("./data/logdata.txt", "r") as file:
        logdata = file.read()

    result = []
    ip_user_cache = re.findall("[\d]*.[\d]*.[\d]*.[\d]*\s-\s[\w]*", logdata)
    time = re.findall("\[(.*?)\]", logdata)
    request = re.findall('"(.*?)"', logdata)

    i = 0
    for element in ip_user_cache:
        ip = re.split("[ - ]", element)[0]
        username = re.split("[ - ]", element)[2]
        result.append(
            {"host": ip, "user_name": username, "time": time[i], "request": request[i]}
        )
        i = +1

    return result

    # raise NotImplementedError()


# %%
logs()
