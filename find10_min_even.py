def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    c=0
    ls=[]
    while c<len(data):
        if data[c]%2==0:
            ls.append(data[c])
        c+=1
    a=0
    mi=ls[0]
    while a<len(ls):
        if mi>=ls[a]:
            mi=ls[a]
        a+=1
    return mi
print(find_min_even([1,2,4,5,3,5,6]))