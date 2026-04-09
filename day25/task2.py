# Below Example shows you How Encapsulation works by making the variable private and then accessing it through a getter method.

class Student: 
    __rollnumber=1234 # This is a private variable and cannot be accessed outside the class.
    
    def get_rollnumber(self):
        self.__rollnumber=5678
        print(self.__rollnumber)



a=Student()
a.get_rollnumber() #This will give an error because the variable is private and cannot be accessed outside the class. To access it, we can use a getter method.
