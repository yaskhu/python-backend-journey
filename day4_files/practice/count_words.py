words=0
with open('practice.txt','r') as file:
    for lines in file:
        for  word in lines:
            words+=1
print(words)