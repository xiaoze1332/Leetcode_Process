taskA, taskB, num = [int(x) for x in input().split(',')]


res = 0
res_list = []

for i in range(num+1):
    res = i * taskA + (num-i) * taskB
    res_list.append(res)

res_list = sorted(list(set(res_list)))

print(res_list)