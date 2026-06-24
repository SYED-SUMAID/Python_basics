import argparse

parser = argparse.ArgumentParser(description="simple calculator")

parser.add_argument("num1",type = float,help = "first number")
parser.add_argument("num2",type = float,help = "second number")

parser.add_argument("operation",choices=["add"],help="operation to perform")

args = parser.parse_args()

if args.operation == "add":
    print(f"the total is {args.num1 + args.num2}")