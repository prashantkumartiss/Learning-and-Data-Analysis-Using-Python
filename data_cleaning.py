"""
Below are functions that aid in managing NA values, renaming columns, filling in cells, and 
replacing values with different entries

"""

# ========= Data Cleaning ========

# set names of columns
df.columns = ['a','b','c']

# check for null values, returns boolean array
pd.isnull()

# returns array that is the opposite of isnull()
pd.notnull()

# drop all rows that contain null values
df.dropna()

# drop columns containing null values
df.dropna(axis=1)

# drop all rows with null values according to a limit
df.dropna(axis=1,thresh=n)

# enters the input x into NA cells
df.fillna(x)

# fill empty values with the mean, so that the mean of the whole is not skewed
s.fillna(s.mean())

# convert datatype of a value to the type entered as the argument
s.astype(float)

# replace value in the first argument place with the second argument
# in this case replaces 1 with 'one'
s.replace(1,'one')

# replace multiple values by entering the input as an array
s.replace([1,3],['one','three'])

# renaming multiple columns
df.rename(columns=lambda x: x + 1)

# renaming certain columns
df.rename(columns={'old_name': 'new_ name'})

# set new index
df.set_index('column_one')

# mass renaming of index
df.rename(index=lambda x: x + 1)










