class A:
    def fun(self):
        print("In class A")

class B(A):
    def fun(self):
        print("In class B")

class C(A):
    def fun(self):
        print("In class C")

class D(B, C):
    pass

obj = D()
obj.fun()

print(D.__mro__)  #this will show the method resolution order for class D, which is D -> B -> C -> A.
print(C.mro())