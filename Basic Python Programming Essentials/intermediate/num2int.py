try:

    count = 0
    user_input = input("Enter a number: ")
    number = int(user_input) #int() to only accept integers, thus,  convert other numbers to integer.
    temp = abs(number) #abs() is used to get the absolute value. i.e. to handle the case even if the number is negative.

    print("{} was recognized as: ".format(user_input), type(user_input), "\n and now converted to proper int format.")
    #type to show what data type the value was.

    while (temp > 0):
        temp = temp //10 #// is an integer division, to prevent float results and just get the whole number.
        count = count + 1

    print("Total number of digits : {}".format(count)) #this manually obtaining number of digits instead of using len().
    #.format() is an f-string which is used for string concatination other than using the plus sign.

    number_in_str_format = str(number) #str convert to string format to be able to index the digits.

except:
    print("\nInvalid value. \nPlease mitigate special characters as well as \ninput a number in either proper format \nor only within thousands. \nThank you.")