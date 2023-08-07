# we use loops to create repetition. 
successful = False # this decides what message given.
for number in range(1,3): # how many times we want it to be repeated.
    print("Attempt", number) # here we write what we want to be repeated 3 times.
    if successful:
        print("Successful")
        break # this breaks the loop.

else:
    print("You have attempted 3 times and failed")
# number is a variable of type integer. this is a for loop and number is a/
#  different value for each iteration.
# range generates numbers starting from an integer and ending at another.

# nested loops are loops in side of each other.
for x in range(5):
    for y in range (3):
        print(f"({x},{y})")
# range is a complex type, it is iterable, so can be used in a for loop.
print(type(range(5)))

for x in "Python":
    print(x)

# we can also iterate over list.
for y in [2, 3, 4, 5]:
    print(y)




   