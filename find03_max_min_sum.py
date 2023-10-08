def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    ma=mi=data[0]
    a=0
    while a<len(data):
        if ma<=data[a]:
            ma=data[a]
        if mi>=data[a]:
            mi=data[a]
        a+=1
    return mi+ma
print(find_max_min_sum([1,2,3,4,5,6,7]))
