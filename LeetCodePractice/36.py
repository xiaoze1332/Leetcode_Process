class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        if self.row_repeat(board) or self.column_repeat(board) or self.block_repeat(board):
            return False
        else:
            return True

    def jungle_repeat(self, input_list):
        input_list = [i for i in input_list if i != '.']
        if len(input_list) == len(set(input_list)):
            return True
        else:
            return False

    def row_repeat(self, board):
        for i in range(9):
            if not self.jungle_repeat(board[i]):
                return True
        return False

    def column_repeat(self, board):
        for i in range(9):
            if not self.jungle_repeat([board[j][i] for j in range(9)]):
                return True
        return False

    def block_repeat(self, board):
        for i in range(3):
            for j in range(3):
                if not self.jungle_repeat([board[3 * i + k][3 * j + l] for k in range(3) for l in range(3)]):
                    return True
        return False