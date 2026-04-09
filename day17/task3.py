class Complex:

    # Constructor
    def __init__(self, real, imag):
     self.real = real
     self.imag = imag

    def __repr__(self):
        return 'Rational(%s, %s)' % (self.real, self.imag)

    def __str__(self):
     return '%s + i%s' % (self.real, self.imag)    


# Driver program to test above
t = Complex(10, 20)

# Same as "print t"
print (str(t))
print (repr(t))