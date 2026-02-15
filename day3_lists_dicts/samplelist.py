items = [1, 1, 2, 3, 4, 5]
freq={}
for item in items:
    freq[item]=freq.get(item,0)+1
print(freq)