grocerry_items = {
    "apple":15,
    "banana":10,
    "eggs":200,
    "chicken":300,
    "bread":60,
    "bakery":300,
    "fish":300,
    

}
cart = {}

def add_to_cart():
    print("--------AVAILIBLE ITEMS--------")
    for item,price in grocerry_items.items():
        print(f"{item} : {price}")
    
    
    choice = input("Enter what you want (or 'done') to exit :")


    if choice == 'done':
        return False
    
    if choice == 'mango':
        print("item discontinued")
        return True
    
    if  choice not in grocerry_items:
        print("\033[93mitem not found \033[0m")
        return True
    
    qty = int(input(f"Enter the quantity of {choice} :"))
    cart[choice] = cart.get(choice,0) + qty
    print(f"added {choice} : {qty} ")


    print("\n------ CART ------")
    for item, q in cart.items():
        print(f"{item} x {q} = {grocerry_items[item] * q}")
    print("------------------\n")

    return True





def generate_bill():
    print("\033[94m-------your bill--------\033[0m")
    total = 0
    for item,qty in cart.items():
        price = grocerry_items[item] *qty
        total += price
        print(f"{item} x {qty} = {price}")
        


    print("---------------------------")
    print(f"total amount = {total}")
        

    if total >300:
        discount = total*0.10
        new_total = total - discount
        print(f"discount (10%) = {discount}")
        print(f"total after discount {new_total}")

    else:
        print("noo discount applied")
       

def main():
    print("\033[96m------welcome to the grocery store------\033[0m")
    while True:
        is_going = add_to_cart()
        if is_going == False:
         break  

    generate_bill()
    print("----Visit again-----")     


main()
              