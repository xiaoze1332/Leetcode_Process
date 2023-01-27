import sys
from math import gcd as gcd

input_num = []

for line in sys.stdin:
    a = line.split()
    input_num.append(a)
    
#print(input_num) # [['4'], ['0', '1'], ['0', '3'], ['2', '1'], ['2', '3']]
devide_num = int(input_num[0][0]) / 2

x_list = []
y_list = []

for i in range(1, len(input_num)):
    x_list.append(int(input_num[i][0]))
    y_list.append(int(input_num[i][1]))

# print(x_list) # [0, 0, 2, 2]
# print(y_list) # [1, 3, 1, 3]

def calculate_line(x_list):
    results_x_list = []
    count = 0
    for x in range(min(x_list), max(x_list)+1):
        for i in range(len(x_list)):
            if count == devide_num:
                results_x_list.append(x)
                count = 0
            elif x > x_list[i]:
                count += 1
    return results_x_list

x = calculate_line(x_list)
y = calculate_line(y_list)


x_result = []
y_result = []

for i in range(len(x)):
    if x[i] not in x_list:
        x_result.append(x[i])
for i in range(len(y)):
    if y[i] not in y_list:
        y_result.append(y[i])


if not x_result:
    print(-1)
elif not y_result:
    print(-1)
else:
    print(y_result[0], x_result[0])
