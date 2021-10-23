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


# write a csv file with a list(1)
# w = list
with open ('filepath', 'w', newline='') as f:
    wt = csv.writer(f)
    for v in w:
        wt.writerow(v)

# write a csv file with a list(2)
with open ('filepath', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)

# Pandas, xlrd, 
import pandas as pd 
a = pd.read_excel('path', sheetname = 'go', skiprows=4)
print(a.shape)

b.to_excel('path(---b.xlsx', index=False)




