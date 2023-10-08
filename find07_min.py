def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    a=0
    mi=data[0]
    while a<len(data):
        if mi>=data[a]:
            mi=data[a]
        a+=1
    return mi
print(find_min([1,2,3,5,6,4,8]))