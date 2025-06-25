# Conditional statements 
# Determine if a year is a leap year using nested conditional stmt

year = int(input("Enter the year: "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year," is a leap year.")
        else:
            print(year," is not a leap year.")
    else:
        print(year," is a leap year.")
else:
    print(year," is not a leap year.")

# Simple calculator 
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
operator=input("Enter the operator(+,-,*,/): ")


if operator == '*':
    product = num1*num2
    print(num1," * ", num2," = ",product)
elif operator == '-':
    difference = num1 - num2
    print(num1," - ", num2," = ",difference)
elif operator == '+':
    sum = num1 + num2
    print(num1," + ", num2," = ",sum)
elif operator == '/':
    if(num2 == 0):
        print("Error: Division by zero.")
    else:
        quotient = num1/num2
        print(num1," / ", num2," = ",quotient)
else:
    print("Invalid operator")