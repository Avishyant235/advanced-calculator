import time
import os
import math


def clear():
    os.system("cls")


def valid():
    print("Welcome to Python Calculator")
    time.sleep(2)
    clear()

    while True:
        use_or_no = input("Do you want to use the calculator? (y/n): ").lower()
        if use_or_no in ["n", "no"]:
            print("Have a good day!!")
            time.sleep(1.5)
            exit()
        elif use_or_no in ["y", "yes"]:
            print("Let's begin...")
            time.sleep(1)
            clear()
            break
        else:
            print("Invalid input. Try again.")

    operation = input("Type an operation (+, -, *, /, %, ^, sqroot): ")
    operand = input("Number1: ")
    operand2 = input("Number2: ")
    num1a = operand.replace(".", "").replace("-", "")
    num2a = operand2.replace(".", "").replace("-", "")

    clear()

    while operation not in ["+", "-", "*", "/", "%", "^", "sqroot"]:
        print("""Please choose among: +, -, *, /, %, ^, sqroot

                +   Addition
                -   Subtraction
                *   Multiplication
                /   Division
                %   Modulo
                ^   Power
                sqroot   Square Root""")
        operation = input("Type a valid operation: ")

    while True:
        if num1a.isdigit() and num2a.isdigit():
            break
        operand = input("Number1: ")
        operand2 = input("Number2: ")
        num1a = operand.replace(".", "").replace("-", "")
        num2a = operand2.replace(".", "").replace("-", "")
        clear()

    return operation, operand, operand2


def calc(operation, operand, operand2):
    num1 = float(operand)
    num2 = float(operand2)

    if operation == "+":
        result = num1 + num2
        expression = f"{num1} + {num2}"
    elif operation == "-":
        result = num1 - num2
        expression = f"{num1} - {num2}"
    elif operation == "*":
        result = num1 * num2
        expression = f"{num1} * {num2}"
    elif operation == "/":
        while True:
            try:
                result = num1 / num2
                expression = f"{num1} / {num2}"
                break
            except ZeroDivisionError:
                print("Cannot divide by zero. Enter a new Number2.")
                operand2 = input("Number2: ")
                num2 = float(operand2)
    elif operation == "%":
        while True:
            try:
                result = num1 % num2
                expression = f"{num1} % {num2}"
                break
            except ZeroDivisionError:
                print("Cannot modulo by zero. Enter a new Number2.")
                operand2 = input("Number2: ")
                num2 = float(operand2)
    elif operation == "^":
        result = num1 ** num2
        expression = f"{num1} ^ {num2}"
    elif operation == "sqroot":
        while True:
            choice = input("Find square root of Number1 or Number2? (1/2): ")
            if choice == "1":
                while float(operand) < 0:
                    operand = input("Enter a non-negative Number1: ")
                result = math.sqrt(float(operand))
                expression = f"√({operand})"
                break
            elif choice == "2":
                while float(operand2) < 0:
                    operand2 = input("Enter a non-negative Number2: ")
                result = math.sqrt(float(operand2))
                expression = f"√({operand2})"
                break
            else:
                print("Invalid input. Please enter 1 or 2.")

    return result, expression


def simp(expression, result):
    print(f"{expression} = {result:.2f}")
    current_expr = expression
    current_result = result

    while True:
        more = input(
            "Would you like to continue simplifying this expression? (y/n): ").lower()
        if more in ["n", "no"]:
            print(f"Final result: {current_expr} = {current_result:.2f}")
            break

        next_op = input("Next operation (+, -, *, /, %, ^): ")
        while next_op not in ["+", "-", "*", "/", "%", "^"]:
            next_op = input("Invalid. Choose one of (+, -, *, /, %, ^): ")

        new_num = input("Enter the next number: ")
        while not new_num.replace(".", "").replace("-", "").isdigit():
            new_num = input("Invalid. Enter a valid number: ")

        current_expr = f"({current_expr}) {next_op} {new_num}"
        current_result = eval(current_expr.replace("^", "**"))
        print(f"{current_expr} = {current_result:.2f}")


def restart():
    again = input("Would you like to start a new calculation? (y/n): ").lower()
    return again in ["y", "yes"]


while True:
    operation, operand, operand2 = valid()
    result, expression = calc(operation, operand, operand2)
    simp(expression, result)
    if not restart():
        print("Thank you for using the Python Calculator. Goodbye!")
        break
    clear()
