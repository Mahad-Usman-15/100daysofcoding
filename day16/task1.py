# MRO-Method Resolution Order (MRO) defines the order in which Python searches for a method in a class and its parent classes



class Bank:
    def showname(self,name):
        self.name=name
        print(f"The name of the bank is {self.name}")

class Employee(Bank):
    def showname(self,name):
        self.name=name
        print(f"I work in {self.name}.")


bank=Employee()
print(isinstance(bank,Bank))  # This will give true because bank is a subinstance of the Bank Class 
bank.showname("Meezan Bank")        
