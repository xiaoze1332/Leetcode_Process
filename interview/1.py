import sys
from math import gcd as gcd

input_num = []

for line in sys.stdin:
    a = line.split()
    input_num.append(a)

#print(input_num)

total = int(input_num[0][0])

def calculate_inside(a, b, calculate_time):
    results  = []
    for i in range(calculate_time + 1):
        a_tmp = a + i * 1
        b_tmp = b + (calculate_time - i) * 1
        results.append([a_tmp, b_tmp])

    return results

def calculate(input_list):
    calculate_time = int(input_list[-1])
    a = int(input_list[0])
    b = int(input_list[1])

    return calculate_inside(a, b, calculate_time)

#print(calculate(input_num[1]))

results_list = []

for i in range(1, len(input_num)):
    tmp_list = calculate(input_num[i])
    results_list.append(tmp_list)

#print(results_list)

gcd_list1 = []
for i in range(len(results_list)):
    gcd_list1.append([])
    for j in range(len(results_list[i])):
        gcd_list1[i].append(gcd(results_list[i][j][0], results_list[i][j][1]))

#print(gcd_list1)

for i in range(len(gcd_list1)):
    print(max(gcd_list1[i]))
