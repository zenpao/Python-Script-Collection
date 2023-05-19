def grossSalary(name, hour, loan, insurance):
    rate = float(500)
    gross = round(hour * rate, 2)
    tax = round(gross * 0.12, 2)
    print("\nName:", name)
    print("Hour:", int(hour))
    print("\nGross Salary: Php", gross)
    print("\nTax: Php", tax)
    print("Loan: Php", loan)
    print("Insurance: Php", insurance)
    return tax, loan, insurance, gross