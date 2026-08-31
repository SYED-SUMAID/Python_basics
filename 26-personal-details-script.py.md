#  Personal Details Script

## Objective

To create a Python program that accepts personal details from the user and displays them in a structured format.

## Procedure

1. Create a Python file named `26-personal-details-script.py`.
2. Use `input()` to accept the user's personal details.
3. Store the entered information in Variables.
4. Convert the age into an integer using `int()`.
5. Display the details using formatted strings.
6. Run the program and verify the output.

## Description

This program demonstrates the use of variables, `input()`, type conversion, formatted output using f-strings in Python.

## Code

```python

print("===== Personal Details =====")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
college = input("Enter your college: ")
city = input("Enter your city: ")



print("\n===== Personal Details =====")
print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"Course     : {course}")
print(f"College    : {college}")
print(f"City       : {city}")
print("------------------------------")
```

## Output

```text
===== Personal Details =====
Enter your name: Sumaid
Enter your age: 21
Enter your course: B.B.A
Enter your college: ABC College
Enter your city: Srinagar

===== Personal Details =====
Name       : Sumaid
Age        : 21
Course     : B.B.A
College    : ABC College
City       : Srinagar
```
![alt text](<Screenshot (579).png>)
![alt text](<Screenshot (580).png>)

## Conclusion

The Personal Details Script was successfully created using Python. The practical demonstrated user input, variables, type conversion, basic calculations, and formatted output.