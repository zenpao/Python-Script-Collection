class Car:
    color = ""
    model = ""
    manufacturer = ""

car1 = Car()
car2 = Car()
car3 = Car()

car1.color = "Black"
car1.model = "Rush"
car1.manufacturer = "Toyota"
print(f"""
Color: {car1.color}
Model: {car1.model}
Manufacturer: {car1.manufacturer}
""")

car2.color = "Orange"
car2.model = "Elantra"
car2.manufacturer = "Hyundai"
print(f"""
Color: {car2.color}
Model: {car2.model}
Manufacturer: {car2.manufacturer}
""")

car3.color = "Blue"
car3.model = "Spark"
car3.manufacturer = "Chevrolet"
print(f"""
Color: {car3.color}
Model: {car3.model}
Manufacturer: {car3.manufacturer}
""")

