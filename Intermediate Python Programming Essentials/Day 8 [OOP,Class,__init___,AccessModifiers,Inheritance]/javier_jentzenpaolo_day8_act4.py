class House:
    def __init__(self, floorSize, noOfFloors, noOfDoors):
        self.myfloorSize = floorSize
        self.mynoOfFloors = noOfFloors
        self.mynoOfDoors = noOfDoors

    def lightOpen(self):
        print("Light switched-on!")

    def ovenOpen(self):
        print("Oven switched-on!")

    def switchOn(self):
        self.lightOpen()
        self.ovenOpen()

    def properties(self):
        print(f"Floor Size: {self.myfloorSize} sqm")
        print(f"No. of Floors: {self.mynoOfFloors}")
        print(f"No. of Doors: {self.mynoOfDoors}\n")

class TownHouse(House):
    def __init__(self, floorSize, noOfFloors, noOfDoors):
        self.myfloorSize = floorSize
        self.mynoOfFloors = noOfFloors
        self.mynoOfDoors = noOfDoors

house = TownHouse(120.2, 2, 3)
house.properties()
house.switchOn()