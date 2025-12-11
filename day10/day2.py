def countvowels(s):
    vowels = "aeiou"
    vowelcount = 0
    for i in s.lower():
        if i in vowels:
         vowelcount+=1
    return vowelcount
print(countvowels("Hello How are you?"))         

