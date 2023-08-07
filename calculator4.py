def run_match():
    """Function printing python version."""
    num1 = float(input("Enter first number:"))
    operation = input("Enter an operator (+, -, /, *): ")
    num2 = float(input("Enter second number:"))


    match(operation):
        case "+":
            print("Addition of" ,num1, "and" ,num2, "is:", num1 + num2) 
            exit()
        case "-":
            print("Subtraction of" ,num1, "and" ,num2, "is:",num1 - num2 )
            exit()
        case "/":
            print("Division of" ,num1, "and" ,num2, "is:",num1 / num2 )
            exit()
        case "*":
            print("Multiplication of" ,num1, "and" ,num2, "is:",num1 * num2 )
            exit()
        case _:
            print("Error try again")

print(run_match())
