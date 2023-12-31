# another method, using random sample
import random  # import is accessing a package
# to change the length, change the 5 value in brackets
random_list1 = random.sample(range(0, 20), 5)
print(random_list1)

random_list2 = random.sample(range(0, 20), 7)
print(random_list2)

# organise the list from smallest to largest
my_numbers = [14, 0, 5, 10, 8, 18, 17]
my_numbers.sort()  # sorts them in ascending order, [0, 5, 8, 10, 14, 17, 18]
print(my_numbers)

# to sort in descending order:
# gives them in reverse order:[18, 17, 14, 10, 8, 5, 0]
my_numbers.sort(reverse=True)
print(my_numbers)

# formatting your code - look into best practices - look into automated tools 
#autopep8 and pylint
# naming variables - conventions and naming types
# learn what functions are and how to use them
# reorganise code using functions - refactoring
# create a simple calculator using functions - add, subtract, multiply, divide
# learn what pip is and install pandas
# use pandas functions to analyse a data set


# PEP8 standards for formatting code
# for variable names, never use l,i (these look like 1) or o,/
# for example, o=2 because it looks like trying to reassign 0./
#  Using x, y and z is better.
# use underscore for creating multi name variables.
# for single line comments use #, for multi line/block comments use """.
# multi line functions should have indentation of 4 spaces.
# best to have 79 characters per line, to show line continuation use /.
# import new packages on separate lines.
# put a single space around both sides of binary operators such as =.
# but formulas such as x*x or a+b should not have spaces.
# have one statement per line if they are disjointed.

# naming variable conventions:
# use _ to seperate words.
# packages names should all be in lower case.
