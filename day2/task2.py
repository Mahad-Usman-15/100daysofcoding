# Remove duplicate elements from a list while maintaining order.
def remove_duplicate(names: list):
    seen = set()
    result = []
    for name in names:
        if name not in seen:
            seen.add(name)
            result.append(name)
    return result


print(remove_duplicate(["Mahad", 'Areb', 'Mahad']))