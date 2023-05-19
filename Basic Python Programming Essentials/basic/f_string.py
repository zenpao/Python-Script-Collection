x = 10
y = "Zen"
formatted = f"I've told you {x} times already!" #python 3.6+ new F-string method
formatted1 = "I've told you {} times already!".format(x) #python >3.5 new F-string method
formatted2 = "I've told you %d times already!" % (x) #old way but deprecated
formatted3 = "I've told you {} times already!, {}".format(x,y) #python >3.5 new F-string method

print(formatted1 + "\n")

print(formatted2 + "\n")

print(formatted3)