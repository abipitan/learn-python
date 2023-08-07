import pandas as pd
import openpyxl
amazon_df = pd.read_csv("/Users/abi/Documents/PracticePython/Pandas/AmazonDF.csv")
# print(amazon_df)

statistics = amazon_df.describe()
# print(statistics)

# filtering the data
amazon_df.loc(amazon_df["High"] > 110.0)
