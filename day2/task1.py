# Separate even and odd numbers into two different lists from a single list.

def separate__lists(numbers:list):
    evennumbers=[]
    oddnumbers=[]
    for i in numbers:
        if i%2==0:
           evennumbers.append(i)
        else:
           oddnumbers.append(i)
    return evennumbers,oddnumbers

print(separate__lists([1,2,4,5,3,9]))


