import random
import string

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars)for _ in range(length))
    return password

def check_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    length = len(password)

    if length >= 12 and has_upper and has_lower and has_digit and has_symbol:
        return "strong password"
        
    elif length >= 8 and has_upper and has_lower and has_digit :
        return "medium strength"
    
    else:
        return "weak password"
    
def main():
    while True:
        print("---------password Tool---------")
        print("1.generate password")
        print("2.create password")
        print("3.check strength")
        print("4.Exit")

        choice = (input("enter choice :"))

        if choice == '1':
            length =int(input("Enter password length :"))
            pwd = generate_password(length)
            print("generated password:", pwd)

        elif choice == '3':
            print("strength :",check_strength(pwd))  

        elif choice == '2': 
             pwd = input("Enter your password : ")
             print("password saved!") 
        
        elif choice == '4':
            print("goodbye")    
  
        else:
            print("invalid choice")   

main()                  


        
    
    

