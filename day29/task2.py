alphabets="abcdefghijklmnopqrstuvwxyz"
i=0
vowels="aeiou"
while i<26 :
    if alphabets[i] in vowels:
        i+=1
        continue
    
    print(alphabets[i])
    i+=1 

    
