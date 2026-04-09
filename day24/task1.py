# Selection sort
# It is a comparison base sorting
# [sorted,unsorted]
"""
[0,4,4,3,5]

"""

def selectionsort(arr,n):
    for i in range(n):
        minind=i
        for j in range(i+1,n):
            if arr[j]<arr[minind]:
                minind=j
        arr[i], arr[minind] = arr[minind], arr[i]


arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size=len(arr)
selectionsort(arr,size)
print(arr)
