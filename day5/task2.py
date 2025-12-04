start = int(input("Enter the start"))
end = int(input("Enter the end"))

for i in range(start,end+1):
    if start < 1:
        print("invlalid number")
        break
    
    if i%2==0:
        print(i,end=" ")