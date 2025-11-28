# Write a function to check if a number is a prime number.
from math import sqrt
p=0
def IsPrime(num):
   global p
   for i in range(2,num//2+1):
    if num<=1:
     continue
    elif num%i==0:
        p=1
    else:
        p=0       
   if p==1:
    return "The  number is not prime"
   else:
        return "The number is prime"            
print(IsPrime(20))       
