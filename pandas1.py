import pandas as pd

column = ["Batman", "Superman", "Ironman"]
column1 = ["1.8", "1.9", "1.75"]
column2 = ["90", "120", "70"]

titled_columns = {"Superhero": column, "height": column1, 'weight': column2}
data = pd.DataFrame(titled_columns)
print(data)

# manipulate data frame values
bmi = []
# weight/(height**2)
for i in range(len(data)): # to create bmi column we will make a for loop.
    bmi_score = data["weight"][i] + data["height"][i] #bmi score is the weight/
    # value divided by the height.
    # this only works for addition for some reason not any other operation/
    #  also how to get to the power off a value as ** is not accepted?
    bmi.append(bmi_score)


data["bmi"] = bmi
print(data)

# saving the data frame
data.to_csv("bmiPandas.csv", index=False, sep= "\t") # the \t changes what seperates/
# the data values from commos to tabs.
# can also save as txt for example not just csv.