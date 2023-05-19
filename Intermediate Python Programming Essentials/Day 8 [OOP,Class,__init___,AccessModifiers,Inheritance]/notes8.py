class Person:
    def __init__(self, name, address, age):
        self.myname = name
        self.myadd = address
        self.myage = age

    def print1(self):
        print(f"""
        Name: {self.myname}
        Address: {self.myadd}
        Age: {self.myage}
        """)
class Student(Person):
    def __init__(self, name, address, age):
        self.myname = name
        self.myadd = address
        self.myage = age

p1 = Person("Juan", "Tublay", 24)
p1.print1()
s1 = Student("Ana", "Baker", 25)
s1.print1()