import os

file = open("file.txt","r")

print(file.read())
file.close()

file = open("file.txt","a")
file.write("Sige edi huwag!")
file.writelines("asdasdasd")
file.close()

os.remove("file.txt")