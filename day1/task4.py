# Check if a string is a palindrome (e.g., "madam")


def isCheckPalindrome(cleaned_str:str):
    reversedstr=list(cleaned_str)
    reversedstr.reverse()
    return cleaned_str==("".join(reversedstr))
print(isCheckPalindrome("madam"))



