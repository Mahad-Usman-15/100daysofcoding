# Natural Numbers are the numbers that we use for counting. 
# They start from 1 and go on indefinitely. The first few natural numbers are 1, 2, 3, 4, 5, and so on.
def sumNatural(start,end):
    sum=0
    for i in range(start,end+1):
        sum+=i
        
    print(sum)

sumNatural(1,100)        
