import json
import os
import datetime

class Account:
    def __init__(self,acc_no,name,balance,password):
        self.acc_no = acc_no 
        self.name = name
        self.balance = balance
        self.password = password
        self.transactions = []
        self.authenticated = False

        self.created_on = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    def save_to_file(self):
        data = {
            "acc_no": self.acc_no,
            "name": self.name,
            "balance": self.balance,
            "created_on": self.created_on,
            "transactions": self.transactions
        }
        with open(f"{self.acc_no}.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self):
        filename = f"{self.acc_no}.json"

        if not os.path.exists(filename):
            return

        with open("jazzzz.txt", "r") as file:
            data = json.load(file)

            self.balance = data["balance"]
            self.created_on = data["created_on"]
            self.transactions = data["transactions"]

    def authenticate(self):
        if self.authenticated:
            return True

        pwd = input("Enter the password :")
        if pwd == self.password:
            print("\033[96mAccess granted\033[0m")
            self.authenticated = True
            return True 
        else:
            print("Access Denied")
            return False
        
    def add_transaction(self,t_type,amount):
         now = datetime.datetime.now().strftime("%y-%m-%d  %H:%M:%S")
         transaction = {
         "time" : now, 
         "type" : t_type,
         "amount" : amount,
         "balance" : self.balance   
        }
         self.transactions.append(transaction)

    def credit(self,amount):
        if not self.authenticate():
            return
        self.balance += amount
        print(f"RS {amount} were credited.Total balance is {self.balance}")
        self.add_transaction("Credit",amount)

    def debit(self,amount):
        if not self.authenticate():
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        self.balance -= amount
        print(f"Rs {amount} were debited  . Total balance is {self.balance}")
        self.add_transaction("Debit",amount)

    def show_transactions(self):
        print("\033[95mCheck Transaction History\033[0m")
        pwd = input("Enter the Pin : ")  
        
        if pwd != self.password:
            print("Access denied")
            return 
        else:
            print("Access granted")
            
        
        if len(self.transactions) == 0:
            print("No Transactions found")
            return


        print("\033[93mYour Transaction History \033[0m")
        print("-" *40)


        for resources in self.transactions:
            
            print(f"Time:     {resources['time']}")
            print(f"Type:     {resources['type']}")
            print(f"Amount:   {resources['amount']}")
            print(f"Balance:  {resources['balance']}")
            print("-" *40)


    def logout(self):
        caution = input("\033[95mAre you sure you want to log-out (yes or No): \033[0m").lower()
        if caution == "yes":
         self.authenticated = False
         print("Logged out Successfully")
        elif caution == "no":
            self.authenticated = True
            print("Still logged-IN")
            



Sav373 = Account("0173040100049373","Sumaid ALtaf",500000,"99068")
Sav373.credit(5000)
Sav373.debit(599)
Sav373.credit(8000)
Sav373.credit(49999)
Sav373.debit(3099)
Sav373.credit(500)
Sav373.debit(30000)
Sav373.credit(50000)
Sav373.debit(99999)
Sav373.credit(657)
Sav373.debit(7898)
Sav373.show_transactions()


Sav373.logout()



        
                                                   

