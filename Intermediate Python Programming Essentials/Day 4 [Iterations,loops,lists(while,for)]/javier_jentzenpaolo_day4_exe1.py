ctr = 1
sum = 0

while ctr != 6:
    bugs = int(input("Enter number of bugs: "))
    print(f"Day {ctr}: {bugs} bugs \n")
    ctr += 1
    sum += bugs

print("Total bugs:", sum)