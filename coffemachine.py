MENU = {
    "espresso" :{
    "ingredients" :{
        "coffee" : 20,
        "milk" : 150,
        "water" : 100,
        "sugar" : 10,
    },"price" : 150 

},
"latte" :{
    "ingredients" :{
        "coffee" : 30,
        "water" : 150,
        "milk" : 100,
        "sugar" : 20,

    },"price" : 220
},
"cappuccino" :{
    "ingredients" :{
    "coffee" : 50,
    "water" : 80,
    "milk" : 130,
    "sugar" : 40,
    "cream" : 50 
   
   },"price" : 300      

},
}
profit = 0
resources = {
    "water" : 500,
    "coffee" : 130,
    "milk" : 500,
    "sugar" : 80,
    "cream" : 150

}

def is_resource_sufficient(other_ingredients):
  for items in other_ingredients:
    if other_ingredients[items] > resources[items]:
      print(f"sorry not enough{items}")
      return False
  return True
    
def make_money():
 money = int(input("Enter the amount in INR: "))
 return money

def is_transaction_successful(money_recieved,drink_cost):
 if money_recieved >= drink_cost:
  change = round(money_recieved - drink_cost,2)
  print(f"here is your {change} change")
  global profit
  profit += drink_cost
  return True
 else:
  print("sorry not enough money.money refunded")
  return False
   
  
def make_coffee(drink_name,ingredients):
 for items in ingredients:
  resources[items] -= ingredients[items] 
 print(f"here is your {drink_name}.Enjoy your coffee!") 

is_on = True
while is_on:
    choice = input("Enter what do you want(espresso/latte/cappuccino) : ")
    if choice == "off":
     is_on = False

    elif choice == "report":
      print(f"water : {resources['water']}ml") 
      print(f"coffee : {resources['coffee']}gm") 
      print(f"milk : {resources['milk']}ml") 
      print(f"sugar : {resources['sugar']}gm") 
      print(f"cream : {resources['cream']}gm") 
      print(f"money : {profit}")

 

    else:
      drink = MENU.get(choice)


    if drink is None:
      print ("invalid choice")
      continue

    sugar_free = input("do you want it with sugar? (yes/no) : ").lower()


    ingredients = (drink["ingredients"]).copy()


    if sugar_free == "yes":
     if "sugar" in ingredients:
      ingredients["sugar"] = 0
      print("preparing your sugar-free drink")


    elif sugar_free !="no":
      print("preparing your drink with sugar")
      continue

    if is_resource_sufficient(ingredients):
       payment = make_money()
       if is_transaction_successful(payment,drink["price"]):
        make_coffee(choice,ingredients)







