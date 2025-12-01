# Count the occurrences of each character in a string.
def count_occcurences(s):
    chars={}
    for i in s:
        if i in chars:
         chars[i]+=1
        else:
           chars[i]=1
    return chars


print(count_occcurences("a man is heavy"))


        



