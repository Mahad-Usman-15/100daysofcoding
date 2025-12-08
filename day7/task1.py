def find_duplicate(array: list):
    # Use the dictionary 'chars' to store seen elements (the key)
    # and whether they've been encountered (the value).
    seen = set()
    
    for element in array:
        if element in seen:
            # If the element is already in the 'seen' set, it's the first duplicate
            return element
        else:
            # If it's the first time seeing this element, add it to the set
            seen.add(element)
    
    # If the loop completes, no duplicates were found
    return None

print(find_duplicate([1, 2, 2, 3]))
print(find_duplicate([5, 1, 3, 4, 3, 5]))
print(find_duplicate([1, 2, 3, 4]))