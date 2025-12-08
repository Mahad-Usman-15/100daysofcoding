# to check wheter the sequence is arthimetric or not
def is_arthimetric_series(seq:list[int]):
    d1=seq[1]-seq[0]
    d2=seq[2]-seq[1]
    if len(str(seq))<1:
        return False
    if d1!=d2:
        return False
    
    return True    


# Method 2
def is_arthimetric_series(seq: list[int]) -> bool:
    if len(seq) < 2:
        return False
    
    d = seq[1] - seq[0]
    return all(seq[i] - seq[i-1] == d for i in range(1, len(seq)))


print("Arithmetic" if is_arthimetric_series([2, 4, 6, 8, 10]) else "Not Arithmetic")