f = open('24.txt', 'r')
c = 0
for line in f.readlines():
    if line.count('E') < line.count('A'):
        c += 1
print(c)