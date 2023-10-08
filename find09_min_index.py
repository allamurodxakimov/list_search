def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    a=0
    mi=data[0]
    while a<len(data):
        if mi>=data[a]:
            mi=data[a]
        a+=1
    return data.index(mi)
print(find_min_index([-3,2,4,5,-3,2]))

