# Implement a function that calculates the sum of all digits of a number.
# Method1 
sum=0
def sumAllnumbers(num:int):
   global sum
   for i in str(num):
    sum=int(i)+sum
   return sum

print(sumAllnumbers(12345))


# Method2
def sumAllNumbers(num:int):
    global sum
    for i in range(len(str(num))+1):
        sum=i+sum
    return sum    

print(sumAllNumbers(12345))