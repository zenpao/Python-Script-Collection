speed = float(input("Enter speed: "))

if speed >= 24 and speed <= 56:
    print("\nSpeed is normal")
elif speed <= 24 or speed >= 56:
    print("\nSpeed is abnormal")
else:
    print("\nInvalid input")