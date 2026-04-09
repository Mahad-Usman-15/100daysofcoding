# Polymorphism

class Add:
    
    def add(self,ent1,ent2):
        return ent1+ent2

numbers=Add()
print(numbers.add(12,34))    
print(numbers.add("Mahad","Usman"))

# Another example - Method Overriding (Inheritance-based Polymorphism)

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"

class Bird(Animal):
    def speak(self):
        return "Tweet! Tweet!"

# Using polymorphism
animals = [Dog(), Cat(), Bird()]
for animal in animals:
    print(animal.speak())
