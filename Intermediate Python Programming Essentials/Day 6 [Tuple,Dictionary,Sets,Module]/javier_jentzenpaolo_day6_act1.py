record_keeping = {}

def addData():
    keyInput = input("Enter Key: ")
    valueInput = input("Enter Value: ")
    record_keeping[keyInput] = valueInput
    print(record_keeping)

def deleteData():
    keyInput = input("Enter Key to delete: ")
    del record_keeping[keyInput]
    print(record_keeping)

while True:
    print("""
    a. Add Data
    b. Delete Data
    c. End
    """)
    userOption = input("Enter desired option: ")
    if userOption.upper() == "A":
        addData()
        response = str(input("\nDo you want to try again? Y (yes) or N (no): ")).upper()
        if response == 'y':
            continue
        elif response == 'n':
            print("\nThank you!")
            break
        else:
            continue
    elif userOption.upper() == "B":
        deleteData()
        response = str(input("\nDo you want to try again? Y (yes) or N (no): ")).upper()
        if response == 'y':
            continue
        elif response == 'n':
            print("\nThank you!")
            break
        else:
            continue
    elif userOption.upper() == "C":
        print("\nTHANK YOU!")
    else:
        print("Invalid input!")
        break