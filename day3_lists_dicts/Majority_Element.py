def Majority_Element(nums):
    dic={}
    for num in nums:
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1
    n=len(nums)
    b=n/2
    for key,val in dic.items():
        if val > b:
            return key
print(Majority_Element([3,2,3]))