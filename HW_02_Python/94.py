lst=[12,24,35,24,88,120,155,88,120,155]

def duplicateremove(lst):
    newlst=[]
    group = set()
    for item in lst:
        if item not in group:
            group.add( item )
            newlst.append(item)
    return newlst



print(duplicateremove(lst))
