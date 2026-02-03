def even_or_odd(num):
    odd,even=0,0
    while num>0:
        a=num%10
        if a%2==0:
            even+=1
        else:
            odd+=1
        num//=10
    return odd,even
odd,even=even_or_odd(1234)
print(f"Even count is {even} and Odd count is {odd}")