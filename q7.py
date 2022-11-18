from unicodedata import name


class bank:
    
    def init(name, self, balance=0.0):
        self.name = name
        self.balance = balance

        def deposite(self,amount):
            self.amount += amount
            return self.amount

        def withdraw(self,amount):
            if amount>self.balance:
                print("Balance is low...")

            else:
                self.balance -= amount
                return self.balance
        
        def display(self):
            print(self.display)

name = input("ENter your name:")
b = bank()
while(True):
    print("\n D-deposite, W-withdraw, C-display, E-exit")
    ch = input("Enter your choice:")

    if ch=="e" or ch =="E" :
        exit()

    if ch=="d" or ch == "D":
        amt = float(input("Enter amount:"))
        print("Balance after deposite:",b.deposite(amt))

    elif ch == "w" or ch == "W":
        amt = float(input("Enter amount:"))
        print("Balance after withdraw:",b.withdraw(amt))

    elif ch == "c" or ch == "C" :
        b.display()

    else:
        print("Invalid input.....")