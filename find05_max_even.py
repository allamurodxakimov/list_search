def find_max_even(lst):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    a=0
    ls=[]
    while a<len(lst):
        if lst[a]%2==0:
            ls.append(lst[a])
        a+=1
    c=0
    ma=ls[0]
    while c<len(ls):
        if ls[c]>=ma:
            ma=ls[c]
        c+=1
    return ma

print(find_max_even([1,2,3,4,5,6,7]))