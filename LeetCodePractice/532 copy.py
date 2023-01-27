import sys

list = []
list_new = []

for line in sys.stdin:
    list_new = line.split()
    list.append(list_new)
    print(list)


count = 0
visited, unvisited = set(), set()

nums = list[-1].sort()
k = list[0][-1]

nums.sort()
for num in nums:
    if num - k not in visited and num - k in unvisited:
        count += 1
        visited.add(num - k)
    
    unvisited.add(num)

print(count)