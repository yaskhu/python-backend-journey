def anagram(a,b):
    a=sorted(a)
    b=sorted(b)
    if a==b:
        return True
    return False
a="anagram"
b="nagaram"
print(anagram(a,b))