def zeros(lst):
    n=len(lst)
    for i in range(n):
        if lst[i]==0:
            lst.remove(0)
            lst.append(0)
    return lst
print(zeros([0,0,1,2,0,2]))