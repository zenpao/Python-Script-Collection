print("How many kilometers did you cycle today?")
kms = input() #get user input
miles = float(kms)/1.60934 #convert from string to float and divide
miles = round(miles, 2) #round the result
print("\nYour {}km ride was {}mi ".format(kms, miles))

# ROUND SYNTAX:
# round(thing to round, how many decimal points)


