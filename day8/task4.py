def is_anagram(str1, str2):
    str1.split().sort()
    str2.split().sort()
    if str(str1) == str(str2) :
        print("the text is anagram")
    else:
        print("It is not anagram")    

is_anagram("Hello",'Hello')