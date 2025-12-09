# Write a for loop to print the sum of the numbers divisble by 9 between the given range
initial=250
end=355
sum=0
for i in range(initial,end+1):
    if i%9==0:
      sum=sum+i
    else:
       continue
print(sum)