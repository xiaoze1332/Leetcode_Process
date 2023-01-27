import sys
for line in sys.stdin:
    a = line.split()

a = a[0].split(',')

new_dict = {}
for i in a:
    new_dict[i.split(':')[0]] = int(i.split(':')[1])

new_dict_b = sorted(new_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)
new_dict_b = new_dict_b[0:5]

for key, value in new_dict_b:
    print(key, ':', value)