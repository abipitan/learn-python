import pandas as pd

column = ["France", "USA", "UK"]
column2 = ["French", "English", "English"]
column3 = ["hot", "hot", "cold"]
titled_columns = {"country": column,
                  "language": column2,
                    "weather": column3} # dictionary key, can add columns to data frame here
data = pd.DataFrame(titled_columns)

# extracting data
select_column2 = data["language"][1] # can select specific data, 1 indicates the row
select_row = data.iloc[1] # iloc conveys the row 1 is about the USA. 
print(select_row) 



# camelCase
# PascalCase
# snake_case
# kebabe-case