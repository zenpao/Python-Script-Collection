import math

employeeName = str(input("Employee Name: ")).upper()
noHours = int(input("Enter number of hours: "))
sssContribution = int(input("SSS contribution: "))
philHealth = int(input("Phil health: "))
housingLoan = int(input("Housing loan: "))

ratePerHour = 500
grossSalary = float(ratePerHour * noHours)
tax = grossSalary * 0.1
totalDeductions = sssContribution + philHealth + housingLoan + tax
netSalary = grossSalary - totalDeductions

paySlip = f"""
=================PAYSLIP=================
==========EMPLOYEE INFORMATION===========
Employee Name: {employeeName}
Rendered Hours: {noHours}
Rate per Hour: {ratePerHour}
Gross Salary: {grossSalary}
===============DEDUCTIONS================
SSS: {sssContribution}
PhilHealth: {philHealth}
Other Loan: {housingLoan}
Tax: {tax}
Total Deductions: {totalDeductions}
\n
Net Salary: PHP {netSalary}"""


print(paySlip)
