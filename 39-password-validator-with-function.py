def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    if not any(char.isupper() for char in password):
        return "Password must contain an uppercase letter."

    if not any(char.islower() for char in password):
        return "Password must contain a lowercase letter."

    if not any(char.isdigit() for char in password):
        return "Password must contain a number."

    return "Password is valid."


password = input("Enter your password: ")

result = validate_password(password)

print(result)
