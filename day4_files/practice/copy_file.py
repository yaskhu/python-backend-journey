def main(soruce,destination):
    with open(soruce,'r') as file :
        data=file.read()
    with open(destination,'w') as file:
        file.write(data)
main("practice.txt", "output.txt")