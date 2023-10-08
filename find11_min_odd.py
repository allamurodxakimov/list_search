def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    c=0
    ls=[]
    while c<len(data):
        if data[c]%2==1:
            ls.append(data[c])
        c+=1
    a=0
    mi=ls[0]
    while a<len(ls):
        if mi>=ls[a]:
            mi=ls[a]
        a+=1
    return mi
print(find_min_odd([4,5,6,3,8,9]))

