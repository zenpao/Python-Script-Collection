#javier_jentzenpaolo_day
#Philippine Statistics Authortiy - Philippine Identification System (Benguet)
#Cordillera Administrative Region
#Information Systems Analyst I (COSW)

#TUPLE (Tuple uses parethesis while list used brackets)
tup1 = ('physiscs', 'chemistry', 1997, 1998)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]:",tup1[0])
print("tup2[1:5]:",tup2[1:5]) #prints until 5 (minus 1)

print("\n")

#DICTIONARY (Dictionary uses curly braces)
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict)
print("dict['Name']:", dict['Name'])
print("dict['Age']:", dict['Age'])

dict['Age'] = 8
dict['School'] = "DICT"
print(dict)
print("dict['Age']:", dict['Age'])
print(*[str(k) + ':' + str(v) for k,v in dict.items()])

#del dict['Name']
#dict.clear
#del dict

print("\n")

#SETS (Sets uses curly braces but unordered and unindexed)

fruits = {"apple", "banana", "cherry"}
print(fruits)

fruits.add("avocado")
print(fruits)

prog = {"C", "C#", "Java"}
prog.update(["PHP", "Javascript"])
prog.update(["Python"])
print(prog)

fruits.remove("banana")
print(fruits)
fruits.discard("cherry")
print(fruits)

print("\n")

#MODULE