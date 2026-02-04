def Frequency_Analysis(transactions):
    dic={}
    for key in transactions:
        if key in dic:
            dic[key]+=1
        else:
            dic[key]=1
    return dic
print(Frequency_Analysis(["credit", "debit", "credit", "upi", "credit", "upi"]))