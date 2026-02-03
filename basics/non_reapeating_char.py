def nonrepeat(s):
    a=[]
    for char in s:
        if char in a:
            a.remove(char)
        else:
            a.append(char)
    return a[0]
print(nonrepeat('abcdacd'))