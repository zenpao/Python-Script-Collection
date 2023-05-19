office = str(input("Enter Office: ")).upper()
years = int(input("Enter Years in Service: "))

if office == "IT":
    if years >= 10:
        print("Congratulations! Your PBB is amounting to Php 10,000")
    elif years < 10:
        print("Congratulations! Your PBB is amounting to Php 5,000")
elif office == "ACCT":
    if years >= 10:
        print("Congratulations! Your PBB is amounting to Php 12,000")
    elif years < 10:
        print("Congratulations! Your PBB is amounting to Php 6,000")
elif office == "HR":
    if years >= 10:
        print("Congratulations! Your PBB is amounting to Php 15,000")
    elif years < 10:
        print("Congratulations! Your PBB is amounting to Php 7,500")
else:
    print("Office not found.")