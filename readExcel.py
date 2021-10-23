import csv

with open ('filepath', 'r') as f:
    reader = csv.reader(f, delimieter= '|')

    # if you want to delete the column name (header skip!)
    # next(reader)

    for c in reader:
        print(c)

# dictionary type
with open ('filepath', 'r') as f:
    reader = csv.DictReader(f)
    for c in reader:
        for k, v in c.items():
            print(k,v) 
        print ('______________________')


# write a csv file with a list
# w = list
with open ('filepath', 'w', newline='') as f:
    wt = csv.writer(f)
    for v in w:
        wt.writerow(v)

