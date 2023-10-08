def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    ma=data[0]
    a=0
    while a<len(data):
        if data[a]>=ma:
            ma=data[a]
        a+=1
    return ma
print(find_max([1,2,3,4,12,2,6]))
