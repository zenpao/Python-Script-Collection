#javier_jentzenpaolo_day
#Philippine Statistics Authortiy - Philippine Identification System (Benguet)
#Cordillera Administrative Region
#Information Systems Analyst I (COSW)

class Person: #capital 1st letter of classname
    #statements
    lastName = "Castillo"
    firstName = "Daisy Jean"
    middleName = "Abas"

    def printSakalam(self):
        print("Sakalam")

    def printName(self):
        print(self.firstName, self.middleName, self.lastName)

sampleVariable = Person() #put the class inside a variable object
print(sampleVariable.lastName) #call the variable and the method inside the class

print("\n")

sampleVariable2 = Person()
sampleVariable2.lastName = "Javier"
print(sampleVariable.lastName)
print(sampleVariable2.lastName)

sampleVariable.printName()
sampleVariable2.printName()

print("\n")

class Employee:
    def __init__(self, name, email, rph, hw):
        self.myname = name
        self.myemail = email
        self.myrph = rph
        self.myhw = hw

    def computeSalary(self):
        salary = self.myrph * self.myhw
        return salary

    def print1(self):
        print(f"""
        Name: {self.myname}
        Salary: {self.computeSalary()}
        """)

employee1 = Employee("Jentzen Javier", "qroize@gmail.com", 1006, 8)
employee1.print1()

print("\n")

