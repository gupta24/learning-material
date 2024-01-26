# read about the pandas...
import pandas as pd

"""
When working with tabular data, such as data stored in spreadsheets or databases, 
pandas is the right tool for you. pandas will help you to explore, clean, and process your data. In pandas, a data table is called a DataFrame.
"""

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
print(df, end="\n\n")
print(df.Age, end="\n\n")
# we can create series from scratch as well , A pandas Series has no column labels, as it is just a single column of a DataFrame. 
# A Series does have row labels.
ages = pd.Series([22, 35], name="Age")
print(ages, end="\n\n")
# We can do this on the DataFrame by selecting the Age column and applying max():
print("max value is from dataframe :", df.Age.max(), end="\n\n")
# for series
print("max value from series is :", ages.max(), end="\n\n")


"""
Basic statistics (mean, median, min, max, counts…) are easily calculable. These or custom aggregations can be applied on the entire data set, a sliding window of the data, or grouped by categories. 
The latter is also known as the split-apply-combine approach.
"""

# if we are interested in some basic statistics of the numerical data of my data table.
# The describe() method provides a quick overview of the numerical data in a DataFrame. 
# As the Name and Sex columns are textual data, these are by default not taken into account by the describe() method.

statistic_info = df.describe()
print(statistic_info)


"""
pandas supports the integration with many file formats or data sources out of the box (csv, excel, sql, json, parquet,…). 
Importing data from each of these data sources is provided by function with the prefix read_*. Similarly, the to_* methods are used to store data.
"""
# pandas provides the read_csv() function to read data stored as a csv file into a pandas DataFrame
titanic_data = pd.read_csv("/home/rahul/titanic.csv")
print(titanic_data, end="\n\n")
# we can get first 5 rows of a pandas DataFrame.
print(titanic_data.head(5), end="\n\n")
# Interested in the last N rows instead? pandas also provides a tail() method. 
# For example, titanic.tail(10) will return the last 10 rows of the DataFrame.
print(titanic_data.tail(2), end="\n\n")
# to check on how pandas interpreted each of the column data types can be done by requesting the pandas dtypes attribute:
print(titanic_data.dtypes, end="\n\n")
# to get the dataframe inforamation then
print(titanic_data.info(), end="\n\n")
# to set the data into excel sheets
titanic_data.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
# read the excel file
print(pd.read_excel("titanic.xlsx", sheet_name="passengers"), end="\n\n")



"""
Selecting or filtering specific rows and/or columns? 
Filtering the data on a condition? Methods for slicing, selecting, and extracting the data you need are available in pandas.
"""

ages = titanic_data["Age"]
print(ages.head(5), end="\n\n")

# show the type of single coloum as series of row lable.
print(type(titanic_data["Age"]))

# show the type of multiple coloum as dataframe of coloum lable.
print(type(titanic_data[["Name","Age"]]))

# it will give the multiple coloum shape in form of (891, 2)
# basically shape give record and coloum cound in tuple
print(titanic_data[["Age", "Sex"]].shape)

# when we want to get the boolean value that is correct or not.
above = titanic_data["Age"] > 25
print(above, end="\n\n")

# but when we want to filter whole record based on condition then
filter_data = titanic_data[titanic_data["Age"] > 25]
print(filter_data, end="\n\n")

# this given only filter record which is available in list
filter_data = titanic_data[titanic_data["Age"].isin([20,30])]
print(filter_data, end="\n\n")

# its use or condition for filter record from data sheet
class_23 = titanic_data[(titanic_data["Pclass"] == 2) | (titanic_data["Pclass"] == 3)]
print(class_23, end="\n\n")

# it's use for getting the not null value data from the table
age_no_na = titanic_data[titanic_data["Age"].notna()]
print(age_no_na, end="\n\n")

# How do I select specific rows and columns from a DataFrame?
# this is use to find out specific coloum data based on condition.
# In this case, for a subset of both rows and columns is made in one go and just using selection brackets [] is not sufficient anymore. 
# The loc/iloc operators are required in front of the selection brackets []. 
# When using loc/iloc, the part before the comma is the rows you want, and the part after the comma is the columns you want to select.
loc_data = titanic_data.loc[titanic_data["Age"] > 35, "Name"].head(20)
print(loc_data, end="\n\n")

# I’m interested in rows 10 till 25 and columns 3 to 5. than use iloc
iloc_data = titanic_data.iloc[9:25, 2:5]
print(iloc_data, end="\n\n")


"""
pandas provides plotting your data out of the box, using the power of Matplotlib. 
You can pick the plot type (scatter, bar, boxplot,…) corresponding to your data.
"""

"""
There is no need to loop over all rows of your data table to do calculations. Data manipulations on a column work elementwise. 
Adding a column to a DataFrame based on existing data in other columns is straightforward.
"""


"""
Change the structure of your data table in multiple ways. You can melt() your data table from wide to long/tidy form or pivot() 
from long to wide format. With aggregations built-in, a pivot table is created with a single command.
"""

"""
Multiple tables can be concatenated both column wise and row wise as database-like join/merge 
operations are provided to combine multiple tables of data.
"""

"""
pandas has great support for time series and has an extensive set of tools for working with 
dates, times, and time-indexed data.
"""

"""
Data sets do not only contain numerical data. pandas provides a wide range of functions to 
clean textual data and extract useful information from it.
"""


