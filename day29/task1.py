alphabets="abcdefghijklmnopqrstuvwxyz"
vowels="aeiou"
for i in range(26):
    if alphabets[i] in vowels:
        continue
    print(alphabets[i])
    