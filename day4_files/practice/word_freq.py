def file():
    freq={}
    with open('practice.txt','r') as f:
        words=f.read().split()
        for word in words:
            freq[word]=freq.get(word,0)+1
    return freq
print(file())