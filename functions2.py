

def product(*numbers): # *args allows a number of arguements into a function. 
    total = 1 #number of times it totals.
    for number in numbers:
        total *= number
    return total
    
print(product(2, 3, 4, 5))

# we use an * before the parameter name to pass on a variable number of arguments.

    
# make a calculator with functions.
# trying to add with multiple variables.
def sum_the_numbers(*numbers):
    total = 0 # setting intitial total to 0.
    for numb in numbers:
        total += numb # for each number in the loop we add it to the total.
    return total


summation = sum_the_numbers(3, 4)
print(summation)


        
