def find_max_odd(lst):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    a=0
    ls=[]
    while a<len(lst):
        if lst[a]%2==1:
            ls.append(lst[a])
        a+=1
    c=0
    mi=ls[0]
    while c<len(ls):
        if ls[c]>=mi:
            mi=ls[c]
        c+=1
    return mi
print(find_max_odd([1,2,32,4,5,7]))