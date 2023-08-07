# creating functions, use def and then make name.
def print_personal_greeting_message(first_name, last_name):
    """Function printing python version."""
    print(f"Hello there {first_name} {last_name}")
    print("Welcome")  # parts of function are indented.

# camelCase
# PascalCase
# snake_case
# kebabe-case

print_personal_greeting_message("Abisola", "Pitan")  # closing off function
# within the greet() brackets add parameters.
# when you assign values to those parameters they are arguments/
# parameter= input you defins for your funciion.
# f string is used before placeholders for expressions.

# types of functions: 1-perform a task, 2-calculate and return a value.
def get_greeting(name):
    """Function printing python version."""
    return f"Hi {name}"

message = get_greeting("Abi") # called store value in a variable called message.
print(message) # this is useful if need for a file, can print on terminal/
# or use open function to write to a file.

def increment(number, by=1):
    return number + by


print(increment(2, 5))
# this function increases any number you put in by the increment you choose.
# can also make the parameter optional by setting by when definining function.
# all the optional parametrs should be put after the required parameters. 