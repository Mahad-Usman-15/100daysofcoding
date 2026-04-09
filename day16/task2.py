
#  (Diamond Problem)
class A:
    def fun(self):
        print("In class A")

class B(A):
    def fun(self):
        print("In class B")
    

class C(A):
    def fun(self):
        print("In class C")

class D(B,C):  #We can also inherit more than one parent class
    pass

a = D()
a.fun()


# D inherits from B and C.
# Python follows the MRO: D -> B -> C -> A.
# Since B has fun(), it is executed and the search stops.