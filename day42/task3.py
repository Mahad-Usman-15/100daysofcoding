def generate_prime(start,end):
    if start>end:
        start,end=end,start 
    for i in range(start,end+1):
        is_prime = True   #flag
        sqrt=i**0.5
        for j in range(2,int(sqrt)+1):
            if i%j==0:
                is_prime=False
                break
            
        if is_prime :
            print(i)           
            
generate_prime(64,37)