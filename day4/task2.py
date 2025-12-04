# to determine wheter the number is armstrong or not
number = int(input("Enter the number"))
n= number
power = len(str(number))
total = 0
while n > 0:
    digit = n % 10
    total += digit**power
    n//=10

if  total == number:
    print("Armstrong Number")
else:
    print("Not an armstrong number")    