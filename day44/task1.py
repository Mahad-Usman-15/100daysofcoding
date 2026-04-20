n1=int(input("Enter the number"))
n2=int(input("Enter the number"))

def division():
    
 try:
     result=n1 /n2
     return result
 except ZeroDivisionError :
    raise  ZeroDivisionError("sorry")




print(division())