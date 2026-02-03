def check(n):
    if n<=9:
        return True 
    ori=n
    a=0
    while n>0:
        b=n%10
        a=a*10+b
        n//=10
    return ori == a
print(check(123))