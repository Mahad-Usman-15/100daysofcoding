# Implement Inheritance and Polymorphism in a small class hierarchy.

class Animal:
    name:str
    def __init__(self):
        print("hello")

class Dog(Animal):
    def bark(self,name):
        self.name=name
        print(f'{self.name} barks')

dog=Dog()
dog.bark(name="dog")         