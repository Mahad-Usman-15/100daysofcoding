# Generate the first $N$ numbers in the Fibonacci sequence.
def Fabonachhiseries(num,count):
    num1=0
    num2=1
    print(num1)
    print(num2)
    for i in range(num,count+1):
        num=num1+num2
        print(num)
        num1=num2
        num2=num

Fabonachhiseries(7,20)

    