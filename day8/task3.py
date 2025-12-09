# Write a function count_vowels(text) that takes a string and returns the total count of vowels (a, e, i, o, u), being sure to handle both uppercase and lowercase letters.


def count_vowels(text:str):
    vovels="aeiou"
    vovel_count=0
    for char in text:
     if char in vovels:
       vovel_count+=1
    return vovel_count    

print(count_vowels("I am Mahad Usman Studiying in practical senter"))

    