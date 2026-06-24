
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def factor(x,y):
    return x**y
def true_divide(x,y):
    if y==0:
       return "Error! Division by zero"
    return x/y
def floor_divide(x,y):
    return x//y
def modulo_divide(x,y):
    return x%y
print("Simple calculator")
print("Operators: + - * / ** // % ")
while True:
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))
    op = input("Enter operator (+,-,*,/,**,//,%  ):")
    if op == "+":
        print("Result:",add(num1,num2))
    elif op == "-":
        print("Result:",subtract(num1,num2))
    elif op == "*":
        print("Result",multiply(num1,num2))
    elif op == "**":
        print("Result",factor(num1,num2))    
    elif op == "/":
        print("Result",true_divide(num1,num2))
    elif op == "//":
        print("Result",floor_divide(num1,num2))
    elif op == "%":
        print("Result",modulo_divide(num1,num2))
    else:
        print("invalid operator")

    again = input("Do you want to calculate again? (yes or No):").lower()
    if again != "yes":
        break
        