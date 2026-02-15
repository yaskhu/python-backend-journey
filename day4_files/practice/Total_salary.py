import csv
with open('data.csv') as file:
    total=0
    reader=csv.DictReader(file)
    for row in reader:
        total+=int(row['salary'])
print(total)