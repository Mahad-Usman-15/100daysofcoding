# Private,Protected and Public Variables in Python
# Private variables are those that are only accessible within the class they are defined in. They are denoted by a double underscore prefix (e.g., __balance).
#  Protected variables are those that are intended to be accessed only within the class and its subclasses. They are denoted by a single underscore prefix (e.g., _account_number). 
#  Public variables are those that can be accessed from anywhere, both inside and outside the class. They do not have any special prefix (e.g., name).
class Bank:
    def __init__(self, name, balance):
        self.name = name #Public variable
        self.__balance = balance  # Private variable
        self._account_number = "123456789" # Protected variable

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")

mybank=Bank("Mahad",    1000)   
print(mybank.name)  # Accessing public variable
print(mybank.get_balance())  # Accessing private variable through getter method
print(mybank._account_number)  # Accessing protected variable