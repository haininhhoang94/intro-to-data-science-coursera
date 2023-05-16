import csv

# Example to read the csv file
with open("./data/mpg.csv") as csvfile:
    mpg = list(csv.DictReader(csvfile))

# Preview 3 sections of the csv file
mpg[:3]

# Check the length of the csv file
len(mpg)

# Check the list of keys/columns in the csv file
mpg[0].keys()

# This equation: first sum all the number of car available and divide by the
# total number of model (city millage)
# => Average number of car in model
# Instructor version
sum(float(d["cty"]) for d in mpg) / len(mpg)

# My version
sum(float(d["cty"]) for d in mpg) / len(mpg)

##
# This equation: first sum all the number of car available and divide by the
# total number of model (highway)
# => Average number of car in model
sum(float(d["hwy"]) for d in mpg) / len(mpg)

# This equation: first sum all the number of car available and divide by the
# total number of model (number of cylinder (cyl))
# => Average number of car in model
sum(float(d["hwy"]) for d in mpg) / len(mpg)

# Let's group the average number of consume in cylinder
# Let's look at the number of cylinder first
cylinders = set(d["cyl"] for d in mpg)
cylinders

# Set empty list to store the data
CtyMpgByCyl = []

# Loop inside the list cylinder above
for c in cylinders:
    # Create variables summpg and cyltypecount as 0
    # for stacking sum
    summpg = 0
    cyltypecount = 0
    # Loop in each line
    for d in mpg:
        # If cyl belog to a group
        if d["cyl"] == c:
            # Stack summpg
            summpg += float(d["cty"])
            # Increase count when approach a group
            cyltypecount += 1
    # Append cycle count in tuple in array
    CtyMpgByCyl.append((c, summpg / cyltypecount))

# Sort by lambda function, ascending, which sort by key
CtyMpgByCyl.sort(key=lambda x: x[0])
CtyMpgByCyl

# Let's group the average number of consume in vehicle class
# Let's look at the number of cylinder first
vehicle_class = set(d["class"] for d in mpg)
vehicle_class

# Set empty list to store the data
CtyMpgByClass = []

# Loop inside the list cylinder above
for c in vehicle_class:
    # Create variables summpg and cyltypecount as 0
    # for stacking sum
    summpg = 0
    classtypecount = 0
    # Loop in each line
    for d in mpg:
        # If cyl belog to a group
        if d["class"] == c:
            # Stack summpg
            summpg += float(d["cty"])
            # Increase count when approach a group
            classtypecount += 1
    # Append cycle count in tuple in array
    CtyMpgByClass.append((c, summpg / classtypecount))

# Sort by lambda function, ascending, which sort by key
CtyMpgByClass.sort(key=lambda x: x[1])
CtyMpgByClass
