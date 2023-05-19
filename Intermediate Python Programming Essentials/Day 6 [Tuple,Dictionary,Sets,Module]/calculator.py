import operation
#import moduleName as aliasForModule #if you want to use the module for easier encoding
#from moduleName import specificFunction #if you want a specific function in module file

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

operation.add(num1, num2)

print("Sum:", operation.add(num1, num2))
print("Difference:", operation.subtract(num1, num2))
print("Product", operation.multiply(num1, num2))
print("Quotient:", operation.divide(num1, num2))