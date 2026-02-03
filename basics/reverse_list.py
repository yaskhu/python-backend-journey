def reverse(lst):
    n=len(lst)
    j=n-1
    i=0
    while i<j:
        lst[i],lst[j]=lst[j],lst[i]
        j-=1
        i+=1
    return lst
print(reverse([1,2,3,4,5]))