# a python calculator
operator = input("enter the operator you want to perform (+,-,*,/)")
a = int(input("enter the value of a "))
b = int (input ("enter the value of b"))

if operator=="+":
    print(result = round(a + b,2))
elif operator=="-":
    print(result = round(a-b,2))
elif operator =="*":
    print(result = round(a*b,2))
elif operator =="/":
    print(result = round(a/b,2))
else :
    print(f"the operator {operator} is invaid ")

