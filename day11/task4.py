# encapsulation
# Encapsulation is about protecting data inside a class.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age)

# Note: Private properties cannot be accessed directly from outside the class.

class Animal:
  __name:str
  @classmethod
  def showname(cls):
    print(f"I am {cls.__name }")

animal1=Animal()    