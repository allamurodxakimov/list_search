def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    a=0
    ma=data[0]
    while a<len(data):
        if data[a]>=ma:
            ma=data[a]
        a+=1
    return data.count(ma)
print(find_max_count([1,2,3,4,5,1,12,13,9,13,7,13]))

