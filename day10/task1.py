# Swapping of variables

# Method 1
a = 10
b = 20
a=a-b
b=a+b
a=b-a
print(a)
print(b)

# Method 2
a=10
b=20
a,b=b,a
print(a)
print(b)
