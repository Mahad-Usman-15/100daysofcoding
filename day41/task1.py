# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.
def isValid(pin:str)->bool:
    """If the function is passed a valid PIN string, return true, else return false. """
    n=len(pin)
    if n!=4 and n!=6:
        return False
    elif not pin.isdigit():
        return False
    else:
        return True 


print(isValid('134234'))
print(isValid('1234qa'))
print(isValid('123'))

    
    
    