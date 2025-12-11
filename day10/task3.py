# Write a function max_of_three(a, b, c) that takes three numbers and returns the largest one, using only if/elif/else statements (no built-in max() function).

def max_of_three(a, b, c):
    if a>b and a>c:
        print(f"{a} is greatest")
    elif b>a and b>c:
        print(f"{b} is greatest")
    elif c>a and c>b:
        print(f"{c} is greatest")
    else:
        print("Invalid numbers")


max_of_three(1,4,5)        