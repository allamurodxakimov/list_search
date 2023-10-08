def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    a=0
    ma=data[0]
    while a<len(data):
        if ma<=data[a]:
            ma=data[a]
        a+=1
    return data.index(ma)
print(find_max_index([1,2,4,5,6,3,8,5,4,2]))
