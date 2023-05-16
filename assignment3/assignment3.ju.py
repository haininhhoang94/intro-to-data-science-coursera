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

# %% [markdown] deletable=false editable=false nbgrader={"cell_type": "markdown", "checksum": "ab80976c194c2c1bfebb7f3a12fc4e58", "grade": false, "grade_id": "cell-018440ed2f1b6a62", "locked": true, "schema_version": 3, "solution": false}
# # Assignment 3
# All questions are weighted the same in this assignment. This assignment requires more individual learning then the last one did - you are encouraged to check out the [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/) to find functions or methods you might not have used yet, or ask questions on [Stack Overflow](http://stackoverflow.com/) and tag them as pandas and python related. All questions are worth the same number of points except question 1 which is worth 17% of the assignment grade.
#
# **Note**: Questions 2-13 rely on your question 1 answer.

# %%
import pandas as pd
import numpy as np

# Filter all warnings. If you would like to see the warnings, please comment the two lines below.
# import warnings
# warnings.filterwarnings('ignore')


# %% [markdown] deletable=false editable=false nbgrader={"cell_type": "markdown", "checksum": "68063b8b0783f3d8122b516e0cce5f45", "grade": false, "grade_id": "cell-7e5190c7ff1f2e42", "locked": true, "schema_version": 3, "solution": false}
# ### Question 1
# Load the energy data from the file `assets/Energy Indicators.xls`, which is a list of indicators of [energy supply and renewable electricity production](assets/Energy%20Indicators.xls) from the [United Nations](http://unstats.un.org/unsd/environment/excel_file_tables/2013/Energy%20Indicators.xls) for the year 2013, and should be put into a DataFrame with the variable name of **Energy**.
#
# Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:
#
# `['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable]`
#
# Convert `Energy Supply` to gigajoules (**Note: there are 1,000,000 gigajoules in a petajoule**). For all countries which have missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.
#
# Rename the following list of countries (for use in later questions):
#
# ```"Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"```
#
# There are also several countries with parenthesis in their name. Be sure to remove these, e.g. `'Bolivia (Plurinational State of)'` should be `'Bolivia'`.
#
# Next, load the GDP data from the file `assets/world_bank.csv`, which is a csv containing countries' GDP from 1960 to 2015 from [World Bank](http://data.worldbank.org/indicator/NY.GDP.MKTP.CD). Call this DataFrame **GDP**.
#
# Make sure to skip the header, and rename the following list of countries:
#
# ```"Korea, Rep.": "South Korea",
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"```
#
# Finally, load the [Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology](http://www.scimagojr.com/countryrank.php?category=2102) from the file `assets/scimagojr-3.xlsx`, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame **ScimEn**.
#
# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).
#
# The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
#        'Citations per document', 'H index', 'Energy Supply',
#        'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
#        '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
#
# *This function should return a DataFrame with 20 columns and 15 entries, and the rows of the DataFrame should be sorted by "Rank".*

# %% deletable=false nbgrader={"cell_type": "code", "checksum": "57e040f07954f979910eddc0f489ffe5", "grade": false, "grade_id": "cell-bce4d6f2ecdd1297", "locked": false, "schema_version": 3, "solution": true}

# Setup Pandas Dataframe with correct columns and header
Energy = pd.read_excel("./assets/Energy Indicators.xls", skiprows=17).drop(
    columns=["Unnamed: 0", "Unnamed: 1"]
)
Energy.columns = ["Country", "Energy Supply", "Energy Supply per Capita", "% Renewable"]

GDP = pd.read_csv("./assets/world_bank.csv", header=4)

# Remove footer
Energy = Energy[0 : Energy[Energy.isnull().any(axis=1)].reset_index().iloc[0]["index"]]


# %%
def load_dataset():
    import pandas as pd
    import numpy as np

    # Setup Pandas Dataframe with correct columns and header
    Energy = pd.read_excel("./assets/Energy Indicators.xls", skiprows=17).drop(
        columns=["Unnamed: 0", "Unnamed: 1"]
    )
    Energy.columns = [
        "Country",
        "Energy Supply",
        "Energy Supply per Capita",
        "% Renewable",
    ]

    # Remove footer
    Energy = Energy[
        0 : Energy[Energy.isnull().any(axis=1)].reset_index().iloc[0]["index"]
    ]

    # Set N/A for any value contain in every columns
    Energy["Energy Supply"].replace({"...": np.nan}, regex=True, inplace=True)
    Energy["Energy Supply per Capita"].replace(
        {"...": np.nan}, regex=True, inplace=True
    )
    Energy["% Renewable"].replace({"...": np.nan}, regex=True, inplace=True)

    # Test if the replacement is complete?
    # return Energy.loc[Energy.eq("...").any(axis=1)]['Energy Supply']

    # Convert Energy Supply to Gigajoules (there are 10^6 Gigajoules in a Petajoule)
    Energy["Energy Supply"] = Energy["Energy Supply"].apply(lambda x: 10**6 * x)

    # Rename the following list
    # ```"Republic of Korea": "South Korea",
    # "United States of America": "United States",
    # "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    # "China, Hong Kong Special Administrative Region": "Hong Kong"```

    Energy["Country"].replace(
        {"Republic of Korea": "South Korea"}, regex=True, inplace=True
    )
    Energy["Country"].replace(
        {"United States of America": "United States"}, regex=True, inplace=True
    )
    Energy["Country"].replace(
        {"United Kingdom of Great Britain and Northern Ireland": "United Kingdom"},
        regex=True,
        inplace=True,
    )
    Energy["Country"].replace(
        {"China, Hong Kong Special Administrative Region": "Hong Kong"},
        regex=True,
        inplace=True,
    )

    # Remove all number in Country (problem from formatting of the Excel file)
    Energy["Country"].replace({r"\d+": ""}, regex=True, inplace=True)

    # Test if the replacement is complete?
    # return Energy[Energy['Country'].str.contains("Korea")] # no need for regex here
    # return Energy[Energy['Country'].str.contains("United")]
    # return Energy[Energy['Country'].str.contains("China")]

    # There are also several countries with parenthesis in their name. Be sure to remove these, e.g. `'Bolivia (Plurinational State of)'` should be `'Bolivia'`.
    Energy["Country"].replace({r" \(.*\)": ""}, regex=True, inplace=True)

    # Test if the replacement is complete?
    # return Energy[Energy['Country'].str.contains("Bolivia ")]

    # Load the World Bank dataframe
    GDP = pd.read_csv("./assets/world_bank.csv", header=4)

    # Make sure to skip the header, and rename the following list of countries:
    #
    # ```"Korea, Rep.": "South Korea",
    # "Iran, Islamic Rep.": "Iran",
    # "Hong Kong SAR, China": "Hong Kong"```
    GDP["Country Name"].replace(
        {"Korea, Rep.": "South Korea"}, regex=True, inplace=True
    )
    GDP["Country Name"].replace(
        {"Iran, Islamic Rep.": "Iran"}, regex=True, inplace=True
    )
    GDP["Country Name"].replace(
        {"Hong Kong SAR, China": "Hong Kong"}, regex=True, inplace=True
    )

    # Test if the replacement is complete?
    # return GDP[GDP['Country Name'].str.contains("Korea")] # no need for regex here
    # return GDP[GDP['Country Name'].str.contains("Iran")] # no need for regex here
    # return GDP[GDP['Country Name'].str.contains("Hong Kong")] # no need for regex here

    # Load the Sciamgo dataframe
    ScimEn = pd.read_excel("./assets/scimagojr-3.xlsx")

    return (Energy, GDP, ScimEn)


# %%
def answer_one():
    import pandas as pd
    import numpy as np

    # Join the three dataframe above into a new dataset, where we only take top 15 countries by ScimEn. Use only the last 10 years
    # (2006 - 2015) of GDP data
    # The index should be the name of the country, and the columns should be
    # ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
    # 'Citations per document', 'H index', 'Energy Supply',
    # 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
    # '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
    # The result should be a dataframe with 20 cols and 15 entries

    # return ScimEn#.reset_index().columns
    (Energy, GDP, ScimEn) = load_dataset()

    # Merge the ScimEn with GDP, with the following columns
    GDP_cols = [
        "Country Name",
        "2006",
        "2007",
        "2008",
        "2009",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
        "2015",
    ]
    result = pd.merge(
        ScimEn[:15], Energy, how="left", left_on="Country", right_on="Country"
    )
    result = (
        pd.merge(
            result,
            GDP[GDP_cols],
            how="left",
            left_on="Country",
            right_on="Country Name",
        )
        .drop(columns="Country Name")
        .set_index("Country")
    )

    return result


answer_one()
# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "7bcc18b325d2935427ac2566cddd3661", "grade": true, "grade_id": "cell-780b5a4da845dbc3", "locked": true, "points": 5, "schema_version": 3, "solution": false}
assert type(answer_one()) == pd.DataFrame, "Q1: You should return a DataFrame!"

assert answer_one().shape == (
    15,
    20,
), "Q1: Your DataFrame should have 20 columns and 15 entries!"


# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "e241830bcf3f63326b4c9cdf50be8f86", "grade": true, "grade_id": "cell-74b5f0b971379f64", "locked": true, "points": 10, "schema_version": 3, "solution": false}
# Cell for autograder.


# %% [markdown] deletable=false editable=false nbgrader={"cell_type": "markdown", "checksum": "596280cd22ed98c5540580c62954ec2f", "grade": false, "grade_id": "cell-babe0ff2a1fc6b17", "locked": true, "schema_version": 3, "solution": false}
# ### Question 2
# The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
#
# *This function should return a single number.*

# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "c9a34da81c80126fd23ae2eac33f98f8", "grade": false, "grade_id": "cell-96f84e7b693bef63", "locked": true, "schema_version": 3, "solution": false}
# %%HTML
# <svg width="800" height="300">
#   <circle cx="150" cy="180" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="blue" />
#   <circle cx="200" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="red" />
#   <circle cx="100" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="green" />
#   <line x1="150" y1="125" x2="300" y2="150" stroke="black" stroke-width="2" fill="black" stroke-dasharray="5,3"/>
#   <text x="300" y="165" font-family="Verdana" font-size="35">Everything but this!</text>
# </svg>


# %% deletable=false nbgrader={"cell_type": "code", "checksum": "aeeb01fb73054269dd7b818d0945e2f7", "grade": false, "grade_id": "cell-b0c3202c000aada4", "locked": false, "schema_version": 3, "solution": true}
def answer_two_but_wrong():
    # This answer involve at how many entries did you lose
    # Since my answer straightly jump to the answer, let's do something unorthordox
    import pandas as pd
    import numpy as np

    (Energy, GDP, ScimEn) = load_dataset()

    # Merge the ScimEn with GDP, with the following columns
    GDP_cols = [
        "Country Name",
        "2006",
        "2007",
        "2008",
        "2009",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
        "2015",
    ]
    result = pd.merge(ScimEn, Energy, how="left", left_on="Country", right_on="Country")
    result = (
        pd.merge(
            result,
            GDP[GDP_cols],
            how="left",
            left_on="Country",
            right_on="Country Name",
        )
        .drop(columns="Country Name")
        .set_index("Country")
    )

    return result
    # return result.shape[0] - answer_one().shape[0]
    # return answer_one().shape[0]


answer_two_but_wrong()
# %%
def answer_two():
    # This answer involve at how many entries did you lose
    # Since my answer straightly jump to the answer, let's do something unorthordox
    import pandas as pd
    import numpy as np

    (Energy, GDP, ScimEn) = load_dataset()

    GDP.rename(columns={"Country Name": "Country"}, inplace=True)

    # Merge the ScimEn with GDP, with the following columns
    GDP_cols = [
        "Country",
        "2006",
        "2007",
        "2008",
        "2009",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
        "2015",
    ]
    result = pd.merge(ScimEn, Energy, how="outer", on="Country")
    result = pd.merge(
        result,
        GDP[GDP_cols],
        how="outer",
        on="Country",
    ).set_index("Country")

    return result.shape[0] - answer_one().shape[0]


answer_two()


# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "19759b4a6c03f34b647f66d343952619", "grade": true, "grade_id": "cell-be24cfcaa87ab071", "locked": true, "points": 6.66, "schema_version": 3, "solution": false}
assert type(answer_two()) == int, "Q2: You should return an int number!"


# %% [markdown] deletable=false editable=false nbgrader={"cell_type": "markdown", "checksum": "5af1b4f99cd383263130f4c00442a133", "grade": false, "grade_id": "cell-2e54816014e48c18", "locked": true, "schema_version": 3, "solution": false}
# ### Question 3
# What are the top 15 countries for average GDP over the last 10 years?
#
# *This function should return a Series named `avgGDP` with 15 countries and their average GDP sorted in descending order.*


# %% deletable=false nbgrader={"cell_type": "code", "checksum": "a3490fd71a46cecfa3da698e006fe729", "grade": false, "grade_id": "cell-8c3d74335c0d489a", "locked": false, "schema_version": 3, "solution": true}
def answer_three():
    top_15 = answer_one()

    GDP_cols = [
        "2006",
        "2007",
        "2008",
        "2009",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
        "2015",
    ]

    # Taking average
    avgGDP = top_15[GDP_cols].mean(axis=1)

    # Sort
    avgGDP = avgGDP.sort_values(ascending=False)

    return avgGDP


answer_three()

# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "2f9c90ee07138f94c027c5d2f907ab13", "grade": true, "grade_id": "cell-aaaa11ef7d26f4cf", "locked": true, "points": 6.66, "schema_version": 3, "solution": false}
assert type(answer_three()) == pd.Series, "Q3: You should return a Series!"


# %% [markdown]
# ### Question 4
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
#
# *This function should return a single number.*


# %% deletable=false nbgrader={"cell_type": "code", "checksum": "768a19bcc8adc6991fe5c757e95ba784", "grade": false, "grade_id": "cell-7f77d099e3e0bbee", "locked": false, "schema_version": 3, "solution": true}
def answer_four():
    # Let's take the previous answer as a base
    top_15_avg_GDP = answer_three()

    # Let's take the country name
    the_6th = top_15_avg_GDP.index[5]

    # Let's take the whole answer 1 table
    whole = answer_one()

    # Define variable for 2015 and 2006
    GDP_2015 = whole.loc[str(the_6th), "2015"]
    GDP_2006 = whole.loc[str(the_6th), "2006"]

    # return type(GDP_2015)

    # Let's find the_6th 2015 GDP and 2005 GDP
    GDP_difference_for_6th = GDP_2015 - GDP_2006

    return GDP_difference_for_6th


answer_four()

# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "a7770c49cdfac4fa6368dfe8b39e6474", "grade": true, "grade_id": "cell-564dd8e5e24b0f83", "locked": true, "points": 6.66, "schema_version": 3, "solution": false}
# Cell for autograder.


# %% [markdown] deletable=false editable=false nbgrader={"cell_type": "markdown", "checksum": "ed6dbc94ff1b6268873413fee12741cd", "grade": false, "grade_id": "cell-617669111e38ca15", "locked": true, "schema_version": 3, "solution": false}
# ### Question 5
# What is the mean energy supply per capita?
#
# *This function should return a single number.*
# %%
top_15 = answer_one()


# %% deletable=false nbgrader={"cell_type": "code", "checksum": "cfd61a1735889e7ef20692ca0d28ddcb", "grade": false, "grade_id": "cell-58e79d558e982eef", "locked": false, "schema_version": 3, "solution": true}
def answer_five():
    top_15 = answer_one()

    # mean energy supply per capita
    return top_15["Energy Supply per Capita"].mean()


answer_five()


# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "9d61bf22656baeecc77f63d54448590e", "grade": true, "grade_id": "cell-30cc66180851638c", "locked": true, "points": 6.66, "schema_version": 3, "solution": false}
# Cell for autograder.


# %% [markdown] deletable=false editable=false nbgrader={"cell_type": "markdown", "checksum": "2c7a163ae96f56317756456b0d9d695b", "grade": false, "grade_id": "cell-5c11ddd12fd71b3f", "locked": true, "schema_version": 3, "solution": false}
# ### Question 6
# What country has the maximum % Renewable and what is the percentage?
#
# *This function should return a tuple with the name of the country and the percentage.*


# %% deletable=false nbgrader={"cell_type": "code", "checksum": "f8657f18c77eb0f752bca3cc48561da3", "grade": false, "grade_id": "cell-b6824b78e74619f9", "locked": false, "schema_version": 3, "solution": true}
def answer_six():
    top_15 = answer_one()

    # What country has the maximum % Renewable and what is the percentage
    # Result is a tuple with name of country and the percentage

    name_ = top_15["% Renewable"].idxmax()
    values_ = top_15["% Renewable"].max()

    return (name_, values_)


answer_six()

# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "f8b28b0a824a3b76a6244c1273648ccd", "grade": true, "grade_id": "cell-2bd201c5c7bdd80f", "locked": true, "points": 6.66, "schema_version": 3, "solution": false}
assert type(answer_six()) == tuple, "Q6: You should return a tuple!"

assert (
    type(answer_six()[0]) == str
), "Q6: The first element in your result should be the name of the country!"


# %% [markdown] deletable=false editable=false nbgrader={"cell_type": "markdown", "checksum": "a7b561a486a28ee4ba80a40715617c6d", "grade": false, "grade_id": "cell-ddf52a85ad3d5a11", "locked": true, "schema_version": 3, "solution": false}
# ### Question 7
# Create a new column that is the ratio of Self-Citations to Total Citations.
# What is the maximum value for this new column, and what country has the highest ratio?
#
# *This function should return a tuple with the name of the country and the ratio.*


# %% deletable=false nbgrader={"cell_type": "code", "checksum": "e4b1cc5e3deefd24be992fbee18d0e74", "grade": false, "grade_id": "cell-a4f39737f38aa53c", "locked": false, "schema_version": 3, "solution": true}
def answer_seven():
    top_15 = answer_one()
    # Create a new column that is the ratio of Self-Citations to Total Citations.
    # What is the maximum value for this new column, and what country has the highest ratio?
    ratio = top_15["Self-citations"] / top_15["Citations"]

    # result
    max_ = ratio.max()
    country_ = ratio.idxmax()

    return (country_, max_)


answer_seven()
# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "ca448b3a16b65a3a08533cac736cc4d9", "grade": true, "grade_id": "cell-b7a163e9231b88c9", "locked": true, "points": 6.66, "schema_version": 3, "solution": false}
assert type(answer_seven()) == tuple, "Q7: You should return a tuple!"

assert (
    type(answer_seven()[0]) == str
), "Q7: The first element in your result should be the name of the country!"


# %% [markdown] deletable=false editable=false nbgrader={"cell_type": "markdown", "checksum": "7be7b86ee7467539dd88746818c78c0e", "grade": false, "grade_id": "cell-5c89296ab6f94218", "locked": true, "schema_version": 3, "solution": false}
# ### Question 8
#
# Create a column that estimates the population using Energy Supply and Energy Supply per capita.
# What is the third most populous country according to this estimate?
#
# *This function should return the name of the country*


# %% deletable=false nbgrader={"cell_type": "code", "checksum": "9d733b2abf089b1931e2e792ff51d488", "grade": false, "grade_id": "cell-9ca58137846b84d6", "locked": false, "schema_version": 3, "solution": true}
def answer_eight():
    top_15 = answer_one()
    # Create a column that estimates the population using Energy Supply and Energy Supply per capita.
    # What is the third most populous country according to this estimate?
    #
    # *This function should return the name of the country*

    popu = top_15["Energy Supply"] / top_15["Energy Supply per Capita"]

    return popu.sort_values(ascending=False).index[2]


answer_eight()
# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "ba2ad50cf8198767b0bd2f75b8d97e87", "grade": true, "grade_id": "cell-3f3620c88df08b20", "locked": true, "points": 0, "schema_version": 3, "solution": false}
assert type(answer_eight()) == str, "Q8: You should return the name of the country!"


# %% [markdown] deletable=false editable=false nbgrader={"cell_type": "markdown", "checksum": "164cba98164a1045db7de10dd37115c8", "grade": false, "grade_id": "cell-2065207e66e5ec01", "locked": true, "schema_version": 3, "solution": false}
# ### Question 9
# Create a column that estimates the number of citable documents per person.
# What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the `.corr()` method, (Pearson's correlation).
#
# *This function should return a single number.*
#
# *(Optional: Use the built-in function `plot9()` to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)*


# %% deletable=false nbgrader={"cell_type": "code", "checksum": "94e06c4c3a9618b94dbb0e86913b546c", "grade": false, "grade_id": "cell-033679ea456bfb9d", "locked": false, "schema_version": 3, "solution": true}
def answer_nine():
    top_15 = answer_one()
    #
    # *This function should return a single number.*
    #
    # *(Optional: Use the built-in function `plot9()` to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)*

    # Create a column that estimates the number of citable documents per person.
    # Create columns estimate population
    popu = top_15["Energy Supply"] / top_15["Energy Supply per Capita"]
    cite_per_person = top_15["Citable documents"] / popu

    # What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the `.corr()` method, (Pearson's correlation).
    corr_ = cite_per_person.corr(top_15["Energy Supply per Capita"])

    return corr_


answer_nine()


# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "01a146bbcca0fa9c9c13e71ab52e710f", "grade": false, "grade_id": "cell-644824f6c708bf80", "locked": true, "schema_version": 3, "solution": false}
def plot9():
    import matplotlib as plt

    # %matplotlib inline

    Top15 = answer_one()
    Top15["PopEst"] = Top15["Energy Supply"] / Top15["Energy Supply per Capita"]
    Top15["Citable docs per Capita"] = Top15["Citable documents"] / Top15["PopEst"]
    Top15.plot(
        x="Citable docs per Capita",
        y="Energy Supply per Capita",
        kind="scatter",
        xlim=[0, 0.0006],
    )


plot9()
# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "8dced1dde88b6877f89bdec482870476", "grade": true, "grade_id": "cell-3cb5c699065a4a20", "locked": true, "points": 6.66, "schema_version": 3, "solution": false}
assert (
    answer_nine() >= -1.0 and answer_nine() <= 1.0
), "Q9: A valid correlation should between -1 to 1!"


# %% [markdown] deletable=false editable=false nbgrader={"cell_type": "markdown", "checksum": "8af5ffad89be1e5c6292438724d6f8d5", "grade": false, "grade_id": "cell-ad09765e29b91157", "locked": true, "schema_version": 3, "solution": false}
# ### Question 10
# Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
#
# *This function should return a series named `HighRenew` whose index is the country name sorted in ascending order of rank.*


# %% deletable=false nbgrader={"cell_type": "code", "checksum": "340c06bd50a9a027a2190674cfb981b9", "grade": false, "grade_id": "cell-0fdf60e64bf1a4f9", "locked": false, "schema_version": 3, "solution": true}
def answer_ten():
    top_15 = answer_one()
    #
    # *This function should return a series named `HighRenew` whose index is the country name sorted in ascending order of rank.*

    # Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
    # Calculate the median for % Renewable value
    median_ = top_15["% Renewable"].median()

    # Function to decide HighRenew
    is_highrenew = lambda x: 1 if x >= median_ else 0

    # Create new columns
    HighRenew = top_15["% Renewable"].apply(is_highrenew)

    return HighRenew


answer_ten()

# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "f624e6996eca5796eaf27fb4d0593175", "grade": true, "grade_id": "cell-b29a631fd9a7730f", "locked": true, "points": 6.66, "schema_version": 3, "solution": false}
assert type(answer_ten()) == pd.Series, "Q10: You should return a Series!"


# %% [markdown] deletable=false editable=false nbgrader={"cell_type": "markdown", "checksum": "52f682e7066791c34cd3b2402855cbf5", "grade": false, "grade_id": "cell-677c51ba711c3af7", "locked": true, "schema_version": 3, "solution": false}
# ### Question 11
# Use the following dictionary to group the Countries by Continent, then create a DataFrame that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.
#
# ```python
# ContinentDict  = {'China':'Asia',
#                   'United States':'North America',
#                   'Japan':'Asia',
#                   'United Kingdom':'Europe',
#                   'Russian Federation':'Europe',
#                   'Canada':'North America',
#                   'Germany':'Europe',
#                   'India':'Asia',
#                   'France':'Europe',
#                   'South Korea':'Asia',
#                   'Italy':'Europe',
#                   'Spain':'Europe',
#                   'Iran':'Asia',
#                   'Australia':'Australia',
#                   'Brazil':'South America'}
# ```
#
# *This function should return a DataFrame with index named Continent `['Asia', 'Australia', 'Europe', 'North America', 'South America']` and columns `['size', 'sum', 'mean', 'std']`*


# %% deletable=false nbgrader={"cell_type": "code", "checksum": "b55846bc20cd01b0acbcb776504a766d", "grade": false, "grade_id": "cell-a5e0c0df27304f98", "locked": false, "schema_version": 3, "solution": true}
def answer_eleven():
    import pandas as pd
    import numpy as np

    top_15 = answer_one()

    # Population for 15 countries
    popu = top_15["Energy Supply"] / top_15["Energy Supply per Capita"]

    ContinentDict = {
        "China": "Asia",
        "United States": "North America",
        "Japan": "Asia",
        "United Kingdom": "Europe",
        "Russian Federation": "Europe",
        "Canada": "North America",
        "Germany": "Europe",
        "India": "Asia",
        "France": "Europe",
        "South Korea": "Asia",
        "Italy": "Europe",
        "Spain": "Europe",
        "Iran": "Asia",
        "Australia": "Australia",
        "Brazil": "South America",
    }

    groupby_popu = popu.groupby(ContinentDict)

    data = {
        "Continent": groupby_popu.size().index.values,
        "size": groupby_popu.size().values,
        "sum": groupby_popu.sum().values,
        "mean": groupby_popu.mean().values,
        "std": groupby_popu.std().values,
    }

    result = pd.DataFrame(data).set_index("Continent")

    return result
    # Australia and South America only have a single country


answer_eleven()


# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "233318097d9c94fdc87395c967da14c4", "grade": true, "grade_id": "cell-18d1a07971b25743", "locked": true, "points": 6.66, "schema_version": 3, "solution": false}
assert type(answer_eleven()) == pd.DataFrame, "Q11: You should return a DataFrame!"

assert answer_eleven().shape[0] == 5, "Q11: Wrong row numbers!"

assert answer_eleven().shape[1] == 4, "Q11: Wrong column numbers!"


# %% [markdown] deletable=false editable=false nbgrader={"cell_type": "markdown", "checksum": "78d9dbb8ff6e0a1ac1e0d16e026a7d98", "grade": false, "grade_id": "cell-fa26f5c1eac39c6c", "locked": true, "schema_version": 3, "solution": false}
# ### Question 12
# Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?
#
# *This function should return a Series with a MultiIndex of `Continent`, then the bins for `% Renewable`. Do not include groups with no countries.*


# %% deletable=false nbgrader={"cell_type": "code", "checksum": "27eb27ec7a3347530174f7047288a881", "grade": false, "grade_id": "cell-2ecd9a4076abd8f0", "locked": false, "schema_version": 3, "solution": true}
def answer_twelve():
    # Implement the previous groupby
    import pandas as pd
    import numpy as np

    top_15 = answer_one()

    # Population for 15 countries
    renew = pd.DataFrame(top_15["% Renewable"])

    ContinentDict = {
        "China": "Asia",
        "United States": "North America",
        "Japan": "Asia",
        "United Kingdom": "Europe",
        "Russian Federation": "Europe",
        "Canada": "North America",
        "Germany": "Europe",
        "India": "Asia",
        "France": "Europe",
        "South Korea": "Asia",
        "Italy": "Europe",
        "Spain": "Europe",
        "Iran": "Asia",
        "Australia": "Australia",
        "Brazil": "South America",
    }

    # In order to use multiple index in groupby, we need to convert the dict into
    # a columns of top_15
    renew["Continent"] = pd.Series(ContinentDict)

    # NOTE: there is no need to create bins outside of pd.cut()
    # it is automatically being taken care of
    # Create bins array for Renewable percentage, with max ~ 70 and min ~ 0)
    # bins = np.linspace(70, 0, num=5)

    # Cut the Renewable percentage into separate category
    renew["% Renewable"] = pd.cut(renew["% Renewable"], bins=5)

    groupby_renew = renew.groupby(["Continent", "% Renewable"]).size()

    # result = pd.DataFrame(groupby_renew, columns=["Number of countries in Continent"])
    result = groupby_renew
    # Remove all zero's values (remove row contain 0)
    # result = result[(result != 0)]

    # return result
    return pd.Series(result)


answer_twelve()


# %%
# def answer_twelve():
#     # YOUR CODE HERE
#     ContinentDict = {
#         "China": "Asia",
#         "United States": "North America",
#         "Japan": "Asia",
#         "United Kingdom": "Europe",
#         "Russian Federation": "Europe",
#         "Canada": "North America",
#         "Germany": "Europe",
#         "India": "Asia",
#         "France": "Europe",
#         "South Korea": "Asia",
#         "Italy": "Europe",
#         "Spain": "Europe",
#         "Iran": "Asia",
#         "Australia": "Australia",
#         "Brazil": "South America",
#     }

#     Top15 = answer_one()
#     Top15 = Top15.reset_index()
#     Top15["Continent"] = Top15["Country"].map(ContinentDict)

#     Top15["% Renewable"] = pd.cut(Top15["% Renewable"], 5)
#     Top15 = Top15.groupby(["Continent", "% Renewable"]).agg(
#         {"Country": pd.Series.nunique}
#     )
#     Top15 = Top15["Country"].dropna()

#     return Top15


# #     raise NotImplementedError()

# answer_twelve()


# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "48903ccc73403827b7ddbb155783ea14", "grade": true, "grade_id": "cell-6c665602d6babab9", "locked": true, "points": 6.66, "schema_version": 3, "solution": false}
assert type(answer_twelve()) == pd.Series, "Q12: You should return a Series!"

assert len(answer_twelve()) == 25, "Q12: Wrong result numbers!"


# %% [markdown] deletable=false editable=false nbgrader={"cell_type": "markdown", "checksum": "bdfd9b1bb897304b6337fdc47a05967c", "grade": false, "grade_id": "cell-4209a10d8f208739", "locked": true, "schema_version": 3, "solution": false}
# ### Question 13
# Convert the Population Estimate series to a string with thousands separator (using commas). Use all significant digits (do not round the results).
#
# e.g. 12345678.90 -> 12,345,678.90
#
# *This function should return a series `PopEst` whose index is the country name and whose values are the population estimate string*


# %% deletable=false nbgrader={"cell_type": "code", "checksum": "1efd09964334b7d6100d81d4b3ead3e9", "grade": false, "grade_id": "cell-58eb0ee0921d93fb", "locked": false, "schema_version": 3, "solution": true}
def answer_thirteen():
    import pandas as pd
    import numpy as np

    top_15 = answer_one()

    # Population for 15 countries in float
    popu = top_15["Energy Supply"] / top_15["Energy Supply per Capita"]

    # Lambda function to convert to string
    convert_string = lambda x: "{:,}".format(x)

    PopEst = popu.apply(convert_string)

    return PopEst


answer_thirteen()

# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "e014781df77c7edab2a181d2d943be8f", "grade": true, "grade_id": "cell-10fee7228cf973f6", "locked": true, "points": 6.74, "schema_version": 3, "solution": false}
assert type(answer_thirteen()) == pd.Series, "Q13: You should return a Series!"

assert len(answer_thirteen()) == 15, "Q13: Wrong result numbers!"


# %% [markdown] deletable=false editable=false nbgrader={"cell_type": "markdown", "checksum": "61562b9b667bd5efbcec0dcd7becbfaa", "grade": false, "grade_id": "cell-998b62d4f390ef15", "locked": true, "schema_version": 3, "solution": false}
# ### Optional
#
# Use the built in function `plot_optional()` to see an example visualization.


# %% deletable=false editable=false nbgrader={"cell_type": "code", "checksum": "479786c97cb5f34d07231c6d7c602a47", "grade": false, "grade_id": "cell-741fd55ea57cd40a", "locked": true, "schema_version": 3, "solution": false}
def plot_optional():
    import matplotlib as plt

    # %matplotlib inline
    Top15 = answer_one()
    ax = Top15.plot(
        x="Rank",
        y="% Renewable",
        kind="scatter",
        c=[
            "#e41a1c",
            "#377eb8",
            "#e41a1c",
            "#4daf4a",
            "#4daf4a",
            "#377eb8",
            "#4daf4a",
            "#e41a1c",
            "#4daf4a",
            "#e41a1c",
            "#4daf4a",
            "#4daf4a",
            "#e41a1c",
            "#dede00",
            "#ff7f00",
        ],
        xticks=range(1, 16),
        s=6 * Top15["2014"] / 10**10,
        alpha=0.75,
        figsize=[16, 6],
    )

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15["Rank"][i], Top15["% Renewable"][i]], ha="center")

    print(
        "This is an example of a visualization that can be created to help understand the data. \
This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
2014 GDP, and the color corresponds to the continent."
    )


plot_optional()
