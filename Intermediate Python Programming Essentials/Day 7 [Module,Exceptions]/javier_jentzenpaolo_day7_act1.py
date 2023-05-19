import random

firstName = ['Jentzen', 'Paolo', 'Rae', 'Gerard', 'Jude', 'Angel', 'Laribel', 'Angelique', 'Marilyn', 'Rojane']
middleName = ['Ancheta', 'Lee', 'Marcelo', 'Ng', 'Tablazon', 'Calderon', 'Cariño', 'Anananayo', 'Ubas', 'Gomez']
lastName = ['Javier', 'Aquino', 'Lo', 'Ferriol', 'Hernandez', 'Soberano', 'Dominador', 'Aplosen', 'Santiago', 'Suoc']
createdNames = []

def generateName():
    newName = f"{firstName[random.randrange(0,9)]} {middleName[random.randrange(0,9)]} {lastName[random.randrange(0,9)]}"
    createdNames.append(newName)
    print(f"Congratulations! Your new name is", newName)

def displayCreatedNames():
    print("Thank you!", createdNames)

while True:
    response = str(input("\nDo you want to generate a new name? Y (yes) or N (no): ")).upper()
    if response.upper() == 'Y':
        generateName()
        continue
    elif response.upper() == 'N':
        displayCreatedNames()
        break
    else:
        print("Invalid input!")
        displayCreatedNames()
        break