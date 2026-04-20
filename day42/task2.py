nums=[2,4,5,6]
def generate_series(n,end):
 if n>end:
        n,end=end,n 
 for i in range(n,end+1):
     is_divide=True
     for j in nums:
         if i%j==0:
             is_divide=False
             break
     if is_divide:
         print(i)    
         
         
generate_series(10,20)