firstName = str(input("Enter first name:"))
middleInitial = str(input("Enter middle initial:"))
lastName = str(input("Enter last name:"))
currentAge = int(input("Enter your age:"))
ageNextYear = int(currentAge + 1)
birthMonth = str(input("Enter your birth month:"))

string1 = f"""Hi! I am {firstName} {middleInitial} {lastName}.
I am {currentAge} and will be turning {ageNextYear} this coming
{birthMonth}.\n"""

string2 = "Are you doing well?\n"

string3 = "Best regards,\n"

print(string1)
print(string2)
print(string3)
print(f"%28s {firstName} {lastName}")
