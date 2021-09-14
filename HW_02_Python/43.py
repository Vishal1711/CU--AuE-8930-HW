tupl = (1,2,3,4,5,6,7,8,9,10)
lst = list()
for i in tupl:
    if i%2==0:
        lst.append(i)

tupl1 = tuple(lst)
print(tupl1)
