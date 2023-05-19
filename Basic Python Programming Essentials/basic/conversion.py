temp = "javier.jentzenpaolo@gmail.com"
num01 = 1.0
num02 = int(num01)
str01 = str(num01)
str02 = temp.lower()
str03 = temp.upper()

print("{} is of type: {} and will now be converted to {} as {}.".format(num01,type(num01),num02,type(num02)))
print("{} is of type: {} and will now be converted to {} as {}.".format(num01,type(num01),str01,type(str01)))
print("{} is now in lowercase. {} is now in uppercase.".format(str02, str03))
