<<<<<<< HEAD
grocery_store ={
    "apple":39,
    "banana":30,
    "bread":30,
    "milk":60,
    "chicken":300,
    "bakery":400,
    "vegies":50
}
cart = {}

def add_to_cart():
    print("\033[96m-------AVAILIBLE ITEMS---------\033[0m")
    for item,price in grocery_store.items():
        print(f"{item} : {price}")
    # if cart:
    #        print("\n\033[93mCurrent cart (item : qty):\033[0m")
    #        for item, qty in cart.items():
    #          print(f"{item} : {qty}")
    # else:
    #  print("\n\033[93mYour cart is empty.\033[0m")

    choice = input("Enter what you want (or/'done') to exit :")   

    if choice == 'done':
        return False
        
    if not choice in grocery_store:
        print("\033[92m--------Item not found--------\033[0m")
        return True
        
    qty = int(input(f"Enter the qty of {choice} : "))
    cart[choice] = cart.get(choice,0) + qty
    print(f"added  {choice} : {qty}")
    return True

def generate_bill():
    print("\033[96m--------YOUR BILL--------\033[0m")
    total = 0
    for item,qty in cart.items():
        price = grocery_store[item]*qty
        total += price
        print(f"{item} x {qty} = {total}")

               
    print("--------TOTAL AMOUNT---------")
    print(f"total amount = {total}")
    

def main():
    print("\033[94m-------WELCOME TO THE GROCERY STORE-------\033[0m")

    while True:
        keep_going = add_to_cart()
        if keep_going == False:
         break

    generate_bill()
    print("\033[94m-------VISIT AGAIN-------\033[0m")


main()
=======
grocery_store ={
    "apple":39,
    "banana":30,
    "bread":30,
    "milk":60,
    "chicken":300,
    "bakery":400,
    "vegies":50
}
cart = {}

def add_to_cart():
    print("\033[96m-------AVAILIBLE ITEMS---------\033[0m")
    for item,price in grocery_store.items():
        print(f"{item} : {price}")
    # if cart:
    #        print("\n\033[93mCurrent cart (item : qty):\033[0m")
    #        for item, qty in cart.items():
    #          print(f"{item} : {qty}")
    # else:
    #  print("\n\033[93mYour cart is empty.\033[0m")

    choice = input("Enter what you want (or/'done') to exit :")   

    if choice == 'done':
        return False
        
    if not choice in grocery_store:
        print("\033[92m--------Item not found--------\033[0m")
        return True
        
    qty = int(input(f"Enter the qty of {choice} : "))
    cart[choice] = cart.get(choice,0) + qty
    print(f"added  {choice} : {qty}")
    return True

def generate_bill():
    print("\033[96m--------YOUR BILL--------\033[0m")
    total = 0
    for item,qty in cart.items():
        price = grocery_store[item]*qty
        total += price
        print(f"{item} x {qty} = {total}")

               
    print("--------TOTAL AMOUNT---------")
    print(f"total amount = {total}")
    

def main():
    print("\033[94m-------WELCOME TO THE GROCERY STORE-------\033[0m")

    while True:
        keep_going = add_to_cart()
        if keep_going == False:
         break

    generate_bill()
    print("\033[94m-------VISIT AGAIN-------\033[0m")


main()
>>>>>>> 56e95cb4badb37c1ed0a73475b8b685a09058e99
