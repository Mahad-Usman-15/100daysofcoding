# Implement a custom function to merge two sorted lists into one sorted list.
def merge(list1:list,list2:list):
    list1.extend(list2)
    return list1
print(merge([123],[123]))


