def userInput():
    while True:
        operation = str(input("""Choose an operation: 
        a. Add
        b. Subtract
        c. Multiple
        d. Divide
        e. Exit
Choice: """))
        if operation.lower() == 'a':
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))
            print(f"Sum of {num1} & {num2}:", addNums(num1, num2))
            tryAgain()
        elif operation.lower() == 'b':
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))
            print(f"Difference of {num1} & {num2}:", subtractNums(num1, num2))
            tryAgain()
        elif operation.lower() == 'c':
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))
            print(f"Product of {num1} & {num2}:", multiplyNums(num1, num2))
            tryAgain()
        elif operation.lower() == 'd':
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))
            if num2 != 0:
                print(f"Quotient of {num1} & {num2}:", divideNums(num1, num2))
                tryAgain()
            else:
                print("""
                Invalid input
                Divisor cannot be zero (0) for division.
                """)
                tryAgain()
        elif operation.lower() == 'e':
            quit()
            break
        else:
            raise Exception
            break

def addNums(num1, num2):
    sum = num1 + num2
    return sum

def subtractNums(num1, num2):
    difference = num1 - num2
    return difference

def multiplyNums(num1, num2):
    product = num1 * num2
    return product

def divideNums(num1, num2):
    quotient = num1 / num2
    return quotient

def tryAgain():
    tryAgainChoice = str(input("\nDo you want to try again? Y (yes) or N (no): "))
    if tryAgainChoice.upper() == 'Y':
        userInput()
    elif tryAgainChoice.upper() == 'N':
        quit()
    else:
        raise Exception

try:
    userInput()
except Exception:
    print("""
    Invalid input
    Use only the appropriate choice for operations.
    """)


