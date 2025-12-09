# Write a function find_smallest(list_of_numbers) that iterates through a list and finds and returns the smallest number

def find_smallest(list_of_numbers:list):
    min=list_of_numbers[0] #any number
    for i in list_of_numbers:
        if i<min:
            min=i
    return min        


print(find_smallest([1234, 435]))