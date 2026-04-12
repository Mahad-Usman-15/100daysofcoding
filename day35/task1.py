# Base class 1
class  A:
    def  a_method(self):
        print('A')

# Base class 2
class  B(A):
    def  a_method(self):
        print('B')
        
# Child class
class  C(B,A): 
    pass
        
c=C()
c.a_method()        