def get_top_k_frequent(items, k):
    freq={}
    for item in items:
        freq[item]=freq.get(item,0)+1 
    sorted_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
    result=[item[0] for item in sorted_freq[:k]]
    return result
items = [1, 1, 1, 2, 2, 3]
k = 2
print(get_top_k_frequent(items,k))