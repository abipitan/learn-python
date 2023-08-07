# simple calculator
from ast import literal_eval

def add_two_numbers(x,y):
    """Function printing python version."""
    return x+y #ADDITION

def subtract_two_numbers(x,y):
    """Function printing python version."""
    return x-y #SUBTRACTION

def multiply_two_numbers(x,y):
    """Function printing python version."""
    return x*y #MULTIPLICATION

def divide_two_numbers(x,y):
    """Function printing python version."""
    return x/y #DIVISION


# menu options
print("Select the number of  the operation you would like to do:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

no1 = literal_eval(input("Enter the first number : ")) # eval() is used so that Python /
# will try and interpret what the user inputs.
no2 = literal_eval(input("Enter the second number : ")) # use literal_eval is safer.

while True: # this is used to run the loop until it breaks.
    choice = int(input("Enter the number of the operation you would like to"
                        "perform from (1, 2, 3, 4): ")) # using int() to convert/
    # value into an integer number.
    if choice in (1, 2, 3, 4): #setting up the if, elif and else.
        if choice == 1: 
            print("Addition of" ,no1, "and" ,no2, "is", add_two_numbers(no1, no2))
            exit() #calculator runs once, the loop does not continue.
        elif choice == 2:
            print("Subtraction of" ,no1, "and" ,no2, "is", subtract_two_numbers(no1, no2))
            exit()
        elif choice == 3:
            print("Multiplication of" ,no1, "and" ,no2, "is", multiply_two_numbers(no1, no2))
            exit()
        elif choice == 4:
            print("Division of" ,no1, "and" ,no2, "is", divide_two_numbers(no1, no2))
            exit()
    else:
            print("Sorry that is not an option try again")

# when there is no docstring need to put "python printing..."


# Learn about switch statements
# DRY


