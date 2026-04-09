# Constructors in Python is use to initialize an object

class Person:
    name="Mahad"
    role="Developer"
    def __init__(self):
        print("Hello I am Ali")
    @classmethod 
    def showname(cls,name,role):
        print(f"My name is {name} and I am {role}")
    


a=Person()
a.name = "Areeb"
a.role="Biomedical Engineer"
a.showname(a.name, a.role)


