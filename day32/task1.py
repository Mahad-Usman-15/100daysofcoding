class Employee:
   def __init__(self,name):
       self.name=name


class  Employee1(Employee):
    def __init__(self,name,age):
        super().__init__(name)  #super() is used to call the parent class's __init__ method to initialize the name attribute.
        self.age=age
        print(f"My name is {self.name} and I am {self.age} years old.")




employee=Employee("John")
employee1=Employee1(employee.name, 30)