def file():
    with open('data.txt','a')as f:
        f.write("\nNew line added")
    return
file()