class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list = []
        for n in range(num):
            list.append([])
            list[n].append(1)
            for i in range(1, n):
                list[n].append(list[n-1][i-1] + list[n-1][i])
            if(n != 0):
                list[n].append(1)

        return list