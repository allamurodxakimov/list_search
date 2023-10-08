def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    a=0
    mi=data[0]
    while a<len(data):
        if mi>=data[a]:
            mi=data[a]
        a+=1
    k=data.count(mi)
    return k
print(find_min_count([2,3,4,-4,3,-4,-4]))
