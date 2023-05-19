import GrossSalary, SalaryDeductions, NetSalary #Note these are file names

def userInput():
    name = str(input("Name: "))
    hour = float(input("Hour: "))
    loan = float(input("Loan: "))
    insurance = float(input("Health Insurance: "))
    return name, hour, loan, insurance

name, hour, loan, insurance = userInput()

tax, loan, insurance, gross = GrossSalary.grossSalary(name, hour, loan, insurance) #after the period are method inside the file

total_deductions = SalaryDeductions.salaryDeductions(tax, loan, insurance)

NetSalary.netSalary(gross, total_deductions)





