MENU = {
    "espresso": {
        "ingredients": {
            "coffee": 20,
            "milk": 150,
            "water": 100,
            "sugar": 10,
        },
        "price": 150
    },

    "latte": {
        "ingredients": {
            "coffee": 30,
            "water": 150,
            "milk": 100,
            "sugar": 20,
        },
        "price": 220
    },

    "cappuccino": {
        "ingredients": {
            "coffee": 50,
            "water": 80,
            "milk": 130,
            "sugar": 40,
            "cream": 50
        },
        "price": 300
    }
}

profit = 0

resources = {
    "water": 500,
    "coffee": 130,
    "milk": 500,
    "sugar": 80,
    "cream": 150
}


def is_resource_sufficient(other_ingredients):
    for item in other_ingredients:
        if other_ingredients[item] > resources[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True


def make_money():
    money = int(input("Enter the amount in INR: "))
    return money


def is_transaction_successful(money_received, drink_cost):
    global profit

    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"Here is your ₹{change} change.")
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"Here is your {drink_name}. Enjoy your coffee!")


is_on = True

while is_on:

    choice = input(
        "Enter what do you want (espresso/latte/cappuccino/report/off): "
    ).lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Coffee : {resources['coffee']}gm")
        print(f"Milk : {resources['milk']}ml")
        print(f"Sugar : {resources['sugar']}gm")
        print(f"Cream : {resources['cream']}gm")
        print(f"Money : ₹{profit}")

    elif choice in MENU:

        drink = MENU[choice]
        ingredients = drink["ingredients"].copy()

        sugar_free = input("Do you want it sugar free? (yes/no): ").lower()

        if sugar_free == "yes":
            ingredients["sugar"] = 0
            print("Preparing your sugar-free drink...")

        elif sugar_free != "no":
            print("Invalid choice.")
            continue

        if is_resource_sufficient(ingredients):
            payment = make_money()

            if is_transaction_successful(payment, drink["price"]):
                make_coffee(choice, ingredients)

    else:
        print("Invalid drink.")