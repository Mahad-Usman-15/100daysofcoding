# Use ternary operator (if/else on one line) to categorize numbers in a list.

def categorize_numbers(numbers:list):
    categories = ['Even' if i % 2 == 0 else 'Odd' for i in numbers]
    return categories

print(categorize_numbers([1,2,3,4,5,6]))