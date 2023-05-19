import os

def addRecord(name, email, address):
    recordBank['Name'] = name
    recordBank['Email'] = email
    recordBank['Address'] = address
    file = open("recordkeep.txt","a")
    toWrite = str(recordBank)[1:-1]
    #file.write("\n")
    #file.write(toWrite)
    file.writelines([toWrite, "\n"])
    file.close()
    viewRecords()

def viewRecords():
    file = open("recordkeep.txt", "r")
    print("\n" + file.read())
    file.close()

def clearAllRecords():
    file = open("recordkeep.txt", "w")
    file.close()
    print("\nNo records found.")

recordBank = {}
choice = str(input("""Choose an operation: 
            a. Add Record
            b. View Records
            c. Clear ALl Records
            d. Exit
Choice: """))
if choice.lower() == 'a':
    name = str(input("Name: "))
    email = str(input("Email: "))
    address = str(input("Address: "))
    addRecord(name, email, address)
elif choice.lower() == 'b':
    viewRecords()
elif choice.lower() == 'c':
    clearAllRecords()
elif choice.lower() == 'd':
    print("\nThank you!")
    quit()
else:
    print("Please enter appropriate entry.")
    quit()





