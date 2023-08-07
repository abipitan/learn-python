# make improvements to this code

# attempting subtraction for multiple numbers.
def sub_the_numbers(*numbers):
    total = 0
    for number in numbers:
        total -= number
    return total


subtraction= sub_the_numbers(10, 5)
print(subtraction)
# issue is these subtract 10 and 5 from 0. Somehow need to make starting/
#  number the one that the user inputs.


# not multiple arguments:

# adding with a fixed number of variables.
def addition(num1, num2):
    sum = num1 + num2
    return sum

print(addition(3, 4))


# subtraction
def subtract(number1, number2):
    answer = number1 - number2
    return(answer)


print(subtract(10,5))
# this one works it returns 5.


# division.
def divide(num1, num2):
    total = num1/num2
    return total

print(divide(20,5))

# multiplication:
def multiply(x,y):
    return x*y

print(multiply(4,5))


