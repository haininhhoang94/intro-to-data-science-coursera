# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] deletable=false editable=false etc_identifier="373a3605-5bda-4e1f-beef-04a0173d3f41" nbgrader={"cell_type": "markdown", "checksum": "ea942292eff37b50f364f842bcdd89", "grade": false, "grade_id": "cell-a839e7b47494b4c3", "locked": true, "schema_version": 3, "solution": false}
# # Assignment 2
#
# For this assignment you'll be looking at 2017 data on immunizations from the CDC. Your datafile for this assignment is in [assets/NISPUF17.csv](assets/NISPUF17.csv). A data users guide for this, which you'll need to map the variables in the data to the questions being asked, is available at [assets/NIS-PUF17-DUG.pdf](assets/NIS-PUF17-DUG.pdf). **Note: you may have to go to your Jupyter tree (click on the Coursera image) and navigate to the assignment 2 assets folder to see this PDF file).**

# %% [markdown] deletable=false editable=false hideCode=false hidePrompt=false nbgrader={"cell_type": "markdown", "checksum": "f85bd44672080d80abd2a7f47aa0f1be", "grade": false, "grade_id": "cell-58fc2e5938733f6a", "locked": true, "schema_version": 3, "solution": false}
# ## Question 1
# Write a function called `proportion_of_education` which returns the proportion of children in the dataset who had a mother with the education levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.
#
# *This function should return a dictionary in the form of (use the correct numbers, do not round numbers):*
# ```
#     {"less than high school":0.2,
#     "high school":0.4,
#     "more than high school but not college":0.2,
#     "college":0.2}
# ```


# %%
# Library
import pandas as pd
import numpy as np
import scipy.stats as stats

# %%
# Load the data first
NISPUF17_dataset = pd.read_csv("./assets/NISPUF17.csv")
NISPUF17_dataset.drop(["Unnamed: 0"], axis=1, inplace=True)
NISPUF17_dataset

# %%
# Since we doesn't have the columns definition, thus we will define the columns by the following dictionary
col_for_NISPIF17 = np.array(NISPUF17_dataset.columns)
np.shape(col_for_NISPIF17)

# %% [markdown]
"""
For question 1, the question only invovle:
- Children has mother with edu level either <,>,=12, >12 but not from a college graduate, and college
- By references of the Page 42 from the PDF, we know that the EDUC1 is the columns we need, thus
and it is category by 4 type:
    * <12
    * 12
    * More than 12 and not college
    * College
"""
# %%
# Let's focus on our columns
education_type_of_mother = NISPUF17_dataset["EDUC1"]
education_type_of_mother.head()

# %%
# Let's do some statistic calculation here to exploring our columns
# Count unique number in the education type columns
education_type_of_mother.nunique(dropna=False)
# this also indicate that there are no N/A value!

# %%
# See which unique values are contained in this series
education_type_of_mother.unique()

# %% [markdown]
"""
As we can see here, there are 4 data types in this series, thus let's define the values
- 1: < 12
- 2: 12
- 3: > 12, not a college graduate
- 4: College graduate
"""


# %% deletable=false nbgrader={"cell_type": "code", "checksum": "0ac58deb3f5ac988c643e903cbee7f3a", "grade": false, "grade_id": "cell-eea16d020eb52ae7", "locked": false, "schema_version": 3, "solution": true}
def proportion_of_education():
    import pandas as pd
    import numpy as np

    df = pd.read_csv("./assets/NISPUF17.csv")
    df.drop(["Unnamed: 0"], axis=1, inplace=True)

    # Let's focus on our columns
    education_type_of_mother = df["EDUC1"]

    # we need a dictionary here, which contain 4 results:
    # less than high school: a
    # high school: b
    # more than high school but not college: c
    # college d
    a = (
        len(education_type_of_mother[1 == education_type_of_mother])
        / education_type_of_mother.count()
    )
    b = (
        len(education_type_of_mother[2 == education_type_of_mother])
        / education_type_of_mother.count()
    )
    c = (
        len(education_type_of_mother[3 == education_type_of_mother])
        / education_type_of_mother.count()
    )
    d = (
        len(education_type_of_mother[4 == education_type_of_mother])
        / education_type_of_mother.count()
    )

    return {
        "less than high school": a,
        "high school": b,
        "more than high school but not college": c,
        "college": d,
    }


proportion_of_education()

# %% deletable=false editable=false hideCode=false hidePrompt=false nbgrader={"cell_type": "code", "checksum": "ac5d91a24a7f72f66c25d242c3d24a50", "grade": true, "grade_id": "cell-c0eeef201366f51c", "locked": true, "points": 1, "schema_version": 3, "solution": false}
assert type(proportion_of_education()) == type({}), "You must return a dictionary."
assert (
    len(proportion_of_education()) == 4
), "You have not returned a dictionary with four items in it."
assert (
    "less than high school" in proportion_of_education().keys()
), "You have not returned a dictionary with the correct keys."
assert (
    "high school" in proportion_of_education().keys()
), "You have not returned a dictionary with the correct keys."
assert (
    "more than high school but not college" in proportion_of_education().keys()
), "You have not returned a dictionary with the correct keys."
assert (
    "college" in proportion_of_education().keys()
), "You have not returned a dictionary with the correct keys."


# %% [markdown]
"""
## Question 2

Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider. Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not.
*This function should return a tuple in the form (use the correct numbers):*
```
(2.5, 0.1)
```
"""
# %% [markdown]
"""
In here, since our interest is based on if the child is:
- Breastfeed or not (CBF-01)
- The number of influenza vaccines (DH1N...)
- The average of the number of influenza vaccines
"""
# %%
# Let's explore each variable:
# 1. Breastfeed
breastfeed = NISPUF17_dataset["CBF_01"]
# Analyze this data first
breastfeed.unique()

# %% [markdown]
"""
As we can see here, the data contains some entries that doesn't fit with out category, 77 and 99
Thus:
"""
# %%
# breastfeed[breastfeed <= 2].unique()
breastfeed = NISPUF17_dataset[NISPUF17_dataset["CBF_01"] <= 2]["CBF_01"]
breastfeed

# %%
# Convert to boolean
# breastfeed = breastfeed.replace(1, 0)
# breastfeed = breastfeed.astype(bool)
# Take sum for total number of children that have breastfeed
# breastfeed_sum = breastfeed.sum()
breastfeed_sum = np.shape(breastfeed[breastfeed == 2])[0]
no_breastfeed_sum = np.shape(breastfeed[breastfeed == 1])[0]
print([breastfeed_sum, no_breastfeed_sum])

# The number of influenza vaccines, which is the following series
# Find the FL(mark for influenza vaccine in dataframe, and see which columns contain it)
# test = (NISPUF17_dataset == "FL").any(axis=0)
# NISPUF17_dataset.columns[test]

# %%
# As we can see here, there are 5 columns contain it, which is:
# 'XFLUTY1', 'XFLUTY2', 'XFLUTY3', 'XFLUTY4', 'XFLUTY5'....
# Based on the PDF references, it is describe as:
# SEASONAL FLU-CONTAINING VACCINATION #1 TYPE CODE
# Let's explore that columns
NISPUF17_dataset["XFLUTY1"]
# So we can safely say that there is 9 entries that can contain a baby vaccine type
# and it is Seasonal

# %%
# Since the question only concern of the average for children who breastfeed or not,
# let's count the number of FL that breastfeed=True
total_influenza = (NISPUF17_dataset == "FL").sum().sum()
# split the count by filter the data and take sum
breastfeed_influenza = (NISPUF17_dataset.set_index("CBF_01").loc[2] == "FL").sum().sum()
no_breastfeed_influenza = (
    (NISPUF17_dataset.set_index("CBF_01").loc[1] == "FL").sum().sum()
)

print([total_influenza, breastfeed_influenza, no_breastfeed_influenza])


# %% deletable=false nbgrader={"cell_type": "code", "checksum": "a405d639063c4a6408365479f29c95c9", "grade": false, "grade_id": "cell-77f18c512324eabb", "locked": false, "schema_version": 3, "solution": true}
def average_influenza_doses():
    import pandas as pd
    import numpy as np

    # Load the data first
    df = pd.read_csv("./assets/NISPUF17.csv")
    df.drop(["Unnamed: 0"], axis=1, inplace=True)

    # Let's do it
    total = df[df["CBF_01"] <= 2]
    breastfeed = total[total["CBF_01"] == 2]
    no_breastfeed = total[total["CBF_01"] == 1]

    # NOTE:using mean to calculate average
    return (no_breastfeed["P_NUMFLU"].mean(), breastfeed["P_NUMFLU"].mean())


average_influenza_doses()

# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "19be955e97fdf7162d43fbb7c2c40951", "grade": true, "grade_id": "cell-54a3ba6cff31caa7", "locked": true, "points": 1, "schema_version": 3, "solution": false}
assert (
    len(average_influenza_doses()) == 2
), "Return two values in a tuple, the first for yes and the second for no."


# %% [markdown] deletable=false editable=false nbgrader={"cell_type": "markdown", "checksum": "e10e2163f5957a0c398ef4f0b76b4efe", "grade": false, "grade_id": "cell-f63377f3c97aa7c4", "locked": true, "schema_version": 3, "solution": false}
# ## Question 3
# It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child. Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex.
#
# *This function should return a dictionary in the form of (use the correct numbers):*
# ```
#     {"male":0.2,
#     "female":0.4}
# ```
#
# Note: To aid in verification, the `chickenpox_by_sex()['female']` value the autograder is looking for starts with the digits `0.0077`.


# %% deletable=false nbgrader={"cell_type": "code", "checksum": "b4d1b58acae002bc73eb0b19f95bc4af", "grade": false, "grade_id": "cell-a0a9e6fe67698006", "locked": false, "schema_version": 3, "solution": true}
def chickenpox_by_sex():
    # There are two variable involve:
    # - (varicella doses) [P_NUMVRC], which return a total number. we only need to see if the child is being vaccinated or not, thus if not = 0 or not N/A
    # - have chickpox? [HAD_CPOX], and 1 is yes, 2 is no
    # - Sex [SEX], 1 is male, 2 is female
    # Return the ratio of (children vaccinated but contracted chickpox / vaccinated and not contract chickpox)
    import pandas as pd

    NISPUF17_dataset = pd.read_csv("./assets/NISPUF17.csv")
    NISPUF17_dataset.drop(["Unnamed: 0"], axis=1, inplace=True)

    male = NISPUF17_dataset.loc[(NISPUF17_dataset["SEX"] == 1)].dropna(
        subset="P_NUMVRC"
    )
    female = NISPUF17_dataset.loc[(NISPUF17_dataset["SEX"] == 2)].dropna(
        subset="P_NUMVRC"
    )

    # for male
    male_varicella = male.loc[(male["P_NUMVRC"] != 0)]

    male_have_chickbox = len(male_varicella.loc[(male_varicella["HAD_CPOX"] == 1)])
    male_no_have_chickbox = len(male_varicella.loc[(male_varicella["HAD_CPOX"] == 2)])

    # for female
    female_varicella = female.loc[(female["P_NUMVRC"] != 0)]

    female_have_chickbox = len(
        female_varicella.loc[(female_varicella["HAD_CPOX"] == 1)]
    )
    female_no_have_chickbox = len(
        female_varicella.loc[(female_varicella["HAD_CPOX"] == 2)]
    )

    return {
        "male": male_have_chickbox / male_no_have_chickbox,
        "female": female_have_chickbox / female_no_have_chickbox,
    }


chickenpox_by_sex()
# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "1b6a113a633c55699ae478a3a9ee9c33", "grade": true, "grade_id": "cell-c4f1714db100c865", "locked": true, "points": 1, "schema_version": 3, "solution": false}
assert (
    len(chickenpox_by_sex()) == 2
), "Return a dictionary with two items, the first for males and the second for females."


# %% [markdown]
# ## Question 4
# A correlation is a statistical relationship between two variables. If we wanted to know if vaccines work, we might look at the correlation between the use of the vaccine and whether it results in prevention of the infection or disease [1]. In this question, you are to see if there is a correlation between having had the chicken pox and the number of chickenpox vaccine doses given (varicella).
#
# Some notes on interpreting the answer. The `had_chickenpox_column` is either `1` (for yes) or `2` (for no), and the `num_chickenpox_vaccine_column` is the number of doses a child has been given of the varicella vaccine. A positive correlation (e.g., `corr > 0`) means that an increase in `had_chickenpox_column` (which means more no’s) would also increase the values of `num_chickenpox_vaccine_column` (which means more doses of vaccine). If there is a negative correlation (e.g., `corr < 0`), it indicates that having had chickenpox is related to an increase in the number of vaccine doses.
#
# Also, `pval` is the probability that we observe a correlation between `had_chickenpox_column` and `num_chickenpox_vaccine_column` which is greater than or equal to a particular value occurred by chance. A small `pval` means that the observed correlation is highly unlikely to occur by chance. In this case, `pval` should be very small (will end in `e-18` indicating a very small number).
#
# [1] This isn’t really the full picture, since we are not looking at when the dose was given. It’s possible that children had chickenpox and then their parents went to get them the vaccine. Does this dataset have the data we would need to investigate the timing of the dose?

# %% deletable=false nbgrader={"cell_type": "code", "checksum": "3e645859949447913cd11d30eb33cb1e", "grade": false, "grade_id": "cell-8afff07f564cf79a", "locked": false, "schema_version": 3, "solution": true}
def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd

    df = pd.read_csv("./assets/NISPUF17.csv")
    # Filter more data
    df = df[df["HAD_CPOX"] <= 2]
    df = df.dropna(subset=["HAD_CPOX", "P_NUMVRC"])

    had_chickenpox = df["HAD_CPOX"]
    num_chickenpox_vaccine = df["P_NUMVRC"]

    # here is some stub code to actually run the correlation
    corr, pval = stats.pearsonr(had_chickenpox, num_chickenpox_vaccine)

    return corr


corr_chickenpox()
# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "ac50ccb747b99f6bbcc76da017e66528", "grade": true, "grade_id": "cell-73408733533a29a5", "locked": true, "points": 1, "schema_version": 3, "solution": false}
assert (
    -1 <= corr_chickenpox() <= 1
), "You must return a float number between -1.0 and 1.0."
