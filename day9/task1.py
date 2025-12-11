import math

start_input = input("Enter the start of the series: ")
end_input = input("Enter the end of the series: ")

try:
    start = int(start_input)
    end = int(end_input)
except ValueError:
    print("Error: Please enter valid integers for the range.")
    exit()

# Logic Fix 1: Ensure start is always the smaller number
if end < start:
    start, end = end, start

primenumbers = []

# Iterate through every number in the specified range
for i in range(start, end + 1):
    
    # Primes must be greater than 1
    if i <= 1:
        continue
    
    # Primes less than 4 (2 and 3)
    if i <= 3:
        primenumbers.append(i)
        continue
    
    # Optimization: All primes greater than 3 are of the form 6k ± 1.
    # We can also check divisibility by 2 and 3 first.
    if i % 2 == 0 or i % 3 == 0:
        continue

    # Assume the number is prime until a factor is found
    is_prime = True

    # Logic Fix 2: Correct range for factor checking (up to sqrt(i))
    # Optimization: Only check divisors up to sqrt(i)
    # Optimization: Only need to check numbers of the form 6k ± 1
    
    # The loop starts checking from 5 (k=1)
    j = 5
    while j * j <= i:
        # Check j (5, 11, 17, 23...)
        if i % j == 0 or i % (j + 2) == 0:
            is_prime = False
            break # Found a factor, stop checking (Early Exit)
        j += 6 # Move to the next 6k ± 1 pair
    
    # Logic Fix 3: Append only if the loop completed without finding a factor
    if is_prime:
        primenumbers.append(i)

print(f"Prime numbers in the range [{start}, {end}]: {primenumbers}")


    
  
