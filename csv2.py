
import csv
gov= [ {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},  
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'} ]
feelds=[]
for govs in gov:
    print(govs.keys())
    feelds=govs.keys()
with open('C:/projects/export.csv', 'w', encoding='utf-8', newline='\n') as f:
    writer = csv.DictWriter(f, feelds,delimiter= ';')
    writer.writeheader()
    for govs in gov:
        writer.writerow(govs)