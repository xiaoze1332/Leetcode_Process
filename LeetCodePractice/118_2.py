class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        num_list = []
        new_list = []

        for n in range(numRows):
            num_list.append(11**n)

        for i in range(len(num_list)):
            new_list.append([])
            for k in str(num_list[i]):
                new_list[i].append(k)

        return new_list