# To determine wwheter the series is gemotric or not
# Method1
def determine_gp(numbers:list):
    r1=numbers[1]/numbers[0]
    r2=numbers[2]/numbers[1]
    if r1==r2:
        print("The series is geometric")
    else:
        print("The series is not geometric")



# To determine whether the series is geometric or not


# Method2
def determine_gp(numbers: list) -> bool:
    """Check if a list of numbers forms a geometric progression."""
    if len(numbers) < 2:
        return False
    
    # Calculate common ratio from first two elements
    if numbers[0] == 0:
        return False
    
    ratio = numbers[1] / numbers[0]
    
    # Check if all consecutive pairs have the same ratio
    for i in range(1, len(numbers) - 1):
        if numbers[i] == 0 or numbers[i+1] / numbers[i] != ratio:
            return False
    
    return True



result = determine_gp([2, 4, 8, 16, 32])
print("The series is geometric" if result else "The series is not geometric")