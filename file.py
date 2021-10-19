# file read 

f = open('filepass', 'r')
content = f.read()
print(content)
f.close()

with open('filepass', 'r') as f:
    c = f.read()
    print(c)

with open('filepass', 'r') as f:
    for c in f:
        print(c.strip())

with open('filepass', 'r') as f:
    line = f.readline()
    while line:
        print(line, end= ' ')
        line = f.readline()

with open('filepass', 'r') as f:
    score = []
    for line in f:
        score.append(int(line))
print("Average : {0}", sum(score)/len(score))

# file write
with open('filepass', 'w') as f: 
    f.write('contents\n')

# file adding
with open('filepass', 'a') as f: 
    f.write('contents2')