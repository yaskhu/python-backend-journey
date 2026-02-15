def file():
    with open('data.txt','r') as f:
        content=f.readlines()
    return content
print(file())