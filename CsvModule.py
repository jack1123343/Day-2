import csv
from os import write

with open ('JackMehoff.csv', 'r') as file :
    reader = csv.reader(file)
    for row in reader :
        print(row)

with open ('Jack.csv', 'w') as file1 :
    writer = csv.writer(file1, delimiter = ':')
    writer.writerow(['Umesh Kumar ', ' 47 ', " Kannur "])
    writer.writerow(['Suresh Babu ', ' 56 ', " Kannur "])

with open('Mehoff.csv', 'w') as file2 :
    fieldnames = ['Name','Age', 'City']
    writer = csv.DictWriter(file2, fieldnames)
    writer.writeheader()
    writer.writerow({'Name':'Umesh Kumar ', 'Age': '50 ', 'City': "Kannur "})
    writer.writerow({'Name': 'Suresh Babu ', 'Age': "56 " , 'City': "Kannur "})

try :
    with open('NonExistant.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except csv.Error as e :
    print(f'Error Reading CSV File : {e}')