# my_function = lambda a, b, c: a + b
# my_function(1, 2, 3)


# Array with people name
people = [
    "Dr. Christopher Brooks",
    "Dr. Kevyn Collins-Thompson",
    "Dr. VG Vinod Vydiswaran",
    "Dr. Daniel Romero",
]


# This function split the title and name of the people above
def split_title_and_name(person):
    return person.split()[0] + " " + person.split()[-1]


# my_func = lambda person: person.split()[0] + " " + person.split()[-1]
# split_title_and_name("Dr. Christopher Brooks") == my_func("Dr. Christopher Brooks")

# option 1
for person in people:
    print(
        split_title_and_name(person)
        == (lambda person: person.split()[0] + " " + person.split()[-1])(person)
    )

# option 2
list(map(split_title_and_name, people)) == list(
    map(lambda person: person.split()[0] + " " + person.split()[-1], people)
)

# List comprehension
my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)

my_list


my_list_comprehension = [number for number in range(0, 1000) if number % 2 == 0]
my_list_comprehension


def times_tables():
    lst = []
    for i in range(10):
        for j in range(10):
            lst.append(i * j)
    return lst


# times_tables()
times_tables() == [i * j for i in range(0, 10) for j in range(0, 10)]

# GRAVEYARD:
# split_title_and_name("Dr. Christopher Brooks")
# list(map(split_title_and_name, people))

# Quiz
"""
Here’s a harder question which brings a few things together.

Many organizations have user ids which are constrained in some way. Imagine you work at an internet service provider and the user ids are all two letters followed by two numbers (e.g. aa49). Your task at such an organization might be to hold a record on the billing activity for each possible user. 

Write an initialization line as a single list comprehension which creates a list of all possible user ids. Assume the letters are all lower case.
"""

lowercase = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"

answer = [
    a + b + c + d for a in lowercase for b in lowercase for c in digits for d in digits
]
answer
# correct_answer == answer
