names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

file = open("app.txt", "w")
file.close()

counter = 0
for elements in names:
    counter += 1
    file = open("app.txt", "a")
    toWrite = elements
    file.write(toWrite)
    file.close()
    print(elements, end=(" " if counter < 6 else "\n"))
    if counter == 6:
        counter = 0
        file = open("app.txt", "a")
        toWrite = "\n"
        file.write(toWrite)
        file.close()

#for letter in name:
#    print(letter, end = " ")

#for i in range(1,10,2): #(start value, max value, skips)
#    print(i, end = " ")