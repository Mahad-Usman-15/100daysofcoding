# Write a function to check if a number is a prime number.
from math import sqrt


def IsPrime(num):
    # Handle edge cases (1 and numbers less than 1)
    if num <= 1:
        return "The number is not prime (by definition)."
    
    # Handle 2 (the only even prime)
    if num == 2:
        return "The number is prime"

    # Optimization: Check divisibility up to sqrt(num)
    # The loop should go from 2 up to int(sqrt(num)) + 1
    # Note: Your original range (num//2) is also a valid check,
    # but sqrt(num) is much more efficient for large numbers.
    # We will use the more efficient sqrt(num) here.
    
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            # Mistake 1 FIX: If a factor is found, it is NOT prime. Return immediately.
            return "The number is not prime"

    # Mistake 2 FIX: If the loop completes without finding any factors, 
    # then the number is prime. This return must be OUTSIDE the loop.
    return "The number is prime"

# Example of why your original code failed:
print(IsPrime(20)) # Output: The number is not prime (Correct)
print(IsPrime(9))  # Output from your original code: "The number is prime" (Incorrect)
print(IsPrime(17)) # Output from your original code: "The number is not prime" (Incorrect, due to logic error)

# Output from the corrected code:
# The number is not prime
# The number is not prime
# The number is prime