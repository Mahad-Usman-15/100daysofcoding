import time
class ATMsimulator:
    def __init__(self,balance,pin):
        print("Welcome to the ATM")
        self.balance=balance
        self.pin=pin
        
    def withdraw(self,amount):
       if amount <= 0:
           print("Invalid amount")
       elif amount > self.balance: 
           print("Insufficient balance")
       else: 
           self.balance -= amount 
           print("Amount withdrawn successfully")

    
    def deposit(self,amount):
        if amount<=0:
            print("Invalid amount")
        else:
           self.balance+=amount
           print("Amount deposited successfully")
            
    
    def showbalance(self):
        print(f"Your Balance:{self.balance}")

    
    


bankaccount = ATMsimulator(10000,123)

pin=int(input("Enter the pin"))
condition=True
if pin==bankaccount.pin:
    while condition:
        print("1.Withdraw")    
        print("2.Deposit ") 
        print("3.Show Balance") 
        print("4.Log out") 
        userchoice=int(input("Enter what you want to do"))
        if userchoice==1:
            useramount=float(input("Enter the amount:"))
            bankaccount.withdraw(useramount)
        elif userchoice==2:
            useramount=float(input("Enter the amount:"))
            bankaccount.deposit(useramount)
        elif userchoice==3:
            bankaccount.showbalance()
        elif userchoice==4:
            print("Logging Out...")  
            time.sleep(1)
            condition=False
        else:
            print("Invalid Choice")
            
else:
    print("Invalid pin")
    
    
    