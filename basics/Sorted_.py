def sorte(lst):
    for i in range(1,len(lst)):
        if lst[i-1]>lst[i]:
            return False
    return True
print(sorte([1,2,4,3]))