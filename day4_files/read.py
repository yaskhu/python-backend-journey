def file(): 
    with open('data.txt','r') as f:
        storage=f.read()
    return storage
print(file())