sum = 0

while True:
    number = int(input("Enter a number: "))
    #check if the number is positive or negative first
    if number > 0: #accepts if the number is positive
        sum += number
    elif number < 0: #ends if the number is negative
        print("Sum of numbers:",sum)
        break #ends the while True condition
