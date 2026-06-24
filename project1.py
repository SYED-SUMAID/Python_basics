class Account:
    def __init__(self,bal,acc_no,password):
        self.bal = bal
        self.acc_no = acc_no
        self.password = str(password)
        self.authenticated = False

    def Authenticate(self):
        if self.authenticated:
            return True
        enter_password = input("Enter the password:")
                 
        if enter_password == str(self.password):
            print("Access granted")
            self.Authenticated = True
            return True
        
        else:
            print("Access denied")
            return False

    def Debit(self,amount): 
        if not self.Authenticate():
            return
        if amount > self.bal:
            print("Insufficient balance")
        else:
            self.bal -= amount

            print(f"Rs {amount} were debited")
            print("Total balance :",self.bal)
    def Credit(self,amount):
        if not self.Authenticate():
         self.bal += amount
        print(f"Rs{amount} were credited")
        print("Total balance :",self.bal)

    def get_bal(self):
        return self.bal
    def get_acc_no(self):
        return self.acc_no  

CC128 = Account(200000,173040100031,6074)
print(CC128.get_bal())
print(CC128.get_acc_no())
CC128.Debit(3900)
CC128.Credit(10000)
CC128.Debit(29999)
CC128.Credit(20000)
CC128.Debit(30000)
CC128            