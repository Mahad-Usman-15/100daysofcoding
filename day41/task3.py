# Complete the square sum function so that it squares each number passed into it and then sums the results together.



def square_sum(numbers):
    squared=[num**2 for num in numbers]
    return sum(squared)


print(square_sum([1, 2, 2]))
print(square_sum([3, 5, 6]))
print(square_sum([10, 5, 7]))

