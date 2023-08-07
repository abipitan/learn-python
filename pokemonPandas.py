import pandas as pd

poke_df = pd.read_csv("/Users/abi/Documents/PracticePython/Pandas/pokemon_data.csv")
# need to put in whole file path.

# print(poke_df.tail(5))
# txt means tab separated format.

# how to print the top few rows: print(poke_df.head(5)). 
# change the number for how many rows you want. 
# for bottom use .tail.

# pd.read_excel to load excel data.
# pd.read_csv("pokemon_data.txt", delimeter ="\t"), need to specify\
# the delimter so that it prints the data with spaces on the terminal.


# reading headers
# print(poke_df.columns) # Index(['#', 'Name', 'Type 1', 'Type 2', 'HP',\
# 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary'],
# dtype='object')

# read each column
# print(poke_df["Name"][0:5]) #gives you top 5 names, can change range.
# can also change column name.

# reading a row:
# print(poke_df.iloc[1:4]) # prints row numbers.

# reading a specific location
# print(poke_df.iloc[2,1]) # prints venusaur

# for index, row in poke_df.iterrows():
   # print(index, row["Name"]) #a way of sorting through the information.
# gives you all the pokemon names e.g. 

# can use .loc as well to find specific data that is more numerical/tectual.

# poke_df_loc = poke_df.loc[poke_df["Type 1"] == "Grass"]
# print(poke_df_loc) 
# prints only the ones that are Grass.

# stats = poke_df.describe() 
# print(stats) # this prints all the mean, percentiles, std.dev etc.

# sorting values.


# making changes to the data.

# adding a column to the data frame.
# poke_df["Total"] = poke_df["HP"] + poke_df["Attack"] + poke_df["Defense"]\
#      + poke_df["Sp. Atk"]+ poke_df["Sp. Def"] + poke_df["Speed"]

# head = poke_df.head(5) 
# print(head)

# dropping a column
# poke_df = poke_df.drop(columns=["Total"])
# head = poke_df.head(5)
# print(head)

# another way to add columns using iloc (integer location)
# poke_df["Total"] = poke_df.iloc[:, 4:10].sum(axis=1)
# use iloc because adding rows, : means all values, 4:10 means\
#  adding those columns, sum means adding those and axis=1 means adding\
# horizontally.



# moving columns
# cols = list(poke_df.columns) # make columns as a list so do not\
# have to type out the names of each column.
# poke_df = poke_df[cols[0:4] + [cols[-1]] + cols[4:12]] #making them as\
# a range, want the first 4 the -1 is reverse indexing so puts the end\
#  column after the first four and then the rest after.
# head = poke_df.head(5)
# print(head)

# import openpyxl 
# poke_df.to_csv("modifiedPokeDF.csv")
# poke_df.to_excel("modifiedPokeDF.xlsx", sheet_name= "modifiedPokeDF" ,index=False)

# filtering data
# filteredPoke = poke_df.loc[(poke_df["Type 1"] == "Fire") |\
#                            (poke_df["Type 2"] == "Poison") & (poke_df["HP"] > 70)]

# using | means or. so either type 1 is fire or type 2 is grass.
# with the filtered data we can see it uses the old index.

# re indexing:
# filteredPoke = filteredPoke.reset_index(drop=True)
# print(filteredPoke) 
# by default it saves old index as a new column so we can get rid of that:
# add drop=True, to do in current data frame get rid of new variable and add\
#  ,inplace=True after drop=True

# nomegadf = poke_df.loc[~poke_df["Name"].str.contains("Mega")]
# ~ means not in python. Can filter our names that contain words.

#REGEX
# import re
# import regular expressions, useful for filtering based on textual patterns.
# regexpoke= poke_df.loc[poke_df["Type 1"].str.contains("Fire|Grass", regex=True)]
# print(regexpoke)
# checking if type 1 equals fire | (means or in regex) grass. 
# if don't have capitals can add, flags=re.I, which means ignore capitals.


# condiitonal changes
# poke_df.loc[poke_df["Type 1"] == "Fire", "Legendary"] = True 
# made it so all fire pokemon are legendary
# poke_df.loc[poke_df["Type 1"] == "Fire", "Type 1"] = "Flamer"
# changed fire to flamer
# poke_df.loc[poke_df["Type 1"] == "Flamer", "Type 1"] = "Fire" # changed back
# print(poke_df)
# can do multiple conditions at once.


# AGGREGATE STATISTICS(GROUPBY)
df = pd.read_csv("modifiedPokeDF.csv")
# df["count"] = 1
# groupeddf = df.groupby(["Type 1", "Type 2"]).count()["count"] # of each type\
# 1 can see what type 2's there are in each. Can do groupby with multiple.
# print(groupeddf)
# can do .mean or .sum or .count
# this gets the count of each type on its own as a column.


# WORKING WITH LARGE AMOUNTS OF DATA
# for df in pd.read_csv("modifiedPokeDF.csv", chunksize = 5):
    # print('CHUNK DF')
    # print(df)
# loads DF in chunks of 5.

new_df = pd.DataFrame(columns=df.columns)# made a blank df
# made a new df with old df's columns.
for df in pd.read_csv("modifiedPokeDF.csv", chunksize = 5):
    results = df.groupby(["Type 1"]).count() # grouped old \
    # df by type 1 and counted the results.
    new_df = pd.concat([new_df, results]) # concat puts 2 df's together.
    print(new_df)
    # then put in chunked data into it with count so can read it better.

