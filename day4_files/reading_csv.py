import csv
def file():
    res=[]
    with open('data.csv','r')as f:
        reader=csv.reader(f)
        for lines in reader:
            print(lines)
file()