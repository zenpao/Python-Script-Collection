class Employee:
    def __init__(self, name, email, mobileNum):
        self.myname = name
        self.myemail = email
        self.mynum = mobileNum

    def printEmployee(self):
        print(f"""
        Name: {self.myname}
        Email: {self.myemail}
        Mobile Number: {self.mynum}
        """)

employee1 = Employee("Jentzen Paolo Javier", "qroize@gmail.com", "09233578994")
employee2 = Employee("Rojane Morales Ferriol", "qroize@yahoo.com", "09973578995")

employee1.printEmployee()
employee2.printEmployee()
