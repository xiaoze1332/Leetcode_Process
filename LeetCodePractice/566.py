class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        r_ori, c_ori = len(mat), len(mat[0])

        if r_ori * c_ori != r * c:
            return mat

        new_list = []
        row = []

        for i in range(r_ori):
            for j in range(c_ori):
                row.append(mat[i][j])
                if len(row) == c:
                    new_list.append(row)
                    row = []

        return new_list
