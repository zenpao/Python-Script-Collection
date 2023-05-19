while True:
    n1 = float(input("\nEnter first: "))
    n2 = float(input("Enter second: "))
    sum = n1 + n2
    print(f"The sum of {n1} and {n2} is: {sum}")
    response = str(input("Do you want to try again? Y (yes) or N (no):")).upper()
    if response == 'Y':
        continue
    elif response == 'N':
        print("\nThank you!")
        break

