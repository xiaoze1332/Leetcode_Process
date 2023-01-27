import sys
for line in sys.stdin:
    a = line.split()

a = int(a[0])

res = []

while a > 4:
    if a % 3 == 0:
        res.append(3)
        a = a - 3
    else:
        a = a - 4
        res.append(4)

   

if a < 4:
    res.append(a)
    #print(a)  

print(res)