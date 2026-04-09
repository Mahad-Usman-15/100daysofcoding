# Sorting is defined as an arrangement of data in a certain order like sorting numbers in increasing order or decreasing order, sorting students by marks and sorting names alphabetically
# bubble sort-sorting a list in aschending order in a way that the corresposing two values are checked iteratively and the largest ones are pushed to the last.
numbers = [90,43,243,32,45]
# pseudocode for bubble sort
# The loop runs n-1 times
"""
for i in range(n):
    for j in range(0,len(numbers)-i-1)

"""


def bubblesort(arr:list[int]):
    n=len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            return   

arr = [64, 34, 25, 12, 22, 11, 90]
bubblesort(arr)
print(arr)



