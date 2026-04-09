# Set 4: The Factor Finder
# Task 1: Input a positive integer ($n$) from the user.
# Task 2: Use a loop to find all numbers from 1 to $n$ that divide $n$ perfectly (factors).
# Task 3: Print each factor found.
# Task 4: Count how many factors the number has and print the result.
# Task 5: Write an algorithm for this task.


n=int(input('Enter the postive integer:'))
count=0
if n>0:

 for i  in range(1,n+1):
    if n%i==0:
        print(i)
        count+=1
  
 print(f"The number had {count} factors")

else:
    print("Enter a positive integer")

print("""
Algorithm for this task
take input from the user
Check whether the user had given a positive integer or not if not so return the message
use for loop to iterate to n from 1
initilize count=0
use if for checking the numbers that are the factors of n
increment count by 1 if factor found
continue in the loop to skip non-factors
print the result
""")
