def Happy_Number(n):
    seen=set()
    while n!=1:
        if n in seen:
            return False
        seen.add(n)
        s=0
        while n>0:
            di=n%10
            s+=di*di
            n//=10
        n==s
    return True
print(Happy_Number(19))