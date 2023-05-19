rectangle1Length = int(input("Enter 1st Rectangle's length: "))
rectangle1Width = int(input("Enter 1st Rectangle's width: "))
rectangle2Length = int(input("Enter 2nd Rectangle's length: "))
rectangle2Width = int(input("Enter 1st Rectangle's width: "))

rectangle1Area = (rectangle1Length * rectangle1Width)
rectangle2Area = (rectangle2Length * rectangle2Width)

if rectangle1Area > rectangle2Area:
    print(f"\nRectangle 1 ({rectangle1Area}) is greater than Rectangle 2 ({rectangle2Area}).")
elif rectangle2Area > rectangle1Area:
    print(f"\nRectangle 2 ({rectangle2Area}) is greater than Rectangle 1 ({rectangle1Area}).")
elif rectangle2Area == rectangle1Area:
    print(f"\nRectangle 1 ({rectangle1Area}) & Rectangle 2 ({rectangle2Area}) are the same.")
else:
    print("\nInvalid input")