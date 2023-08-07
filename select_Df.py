import pandas as pd
# how to get data from other files.
data = pd.read_csv("bmiPandas.csv", sep="\t")
print(data)

# this will print it onto the terminal.