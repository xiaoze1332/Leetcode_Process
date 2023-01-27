import sys
for line in sys.stdin:
    a = line.split()

a = a[0].split(',')
a = [eval(x) for x in a] # [2, 3, 4, 5, 6]

list_len = a.pop(0)

res = []

for i in a:
    if len(res) <= list_len:
        res.append(i)
    else:
        res.pop(0)
        res.append(i)

print(a) 