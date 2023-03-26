class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 0:
            return ''
        if numRows == 1:
            return s
        result = ''
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                j = i
                while j < len(s):
                    result += s[j]
                    j += 2 * numRows - 2
            else:
                j = i
                while j < len(s):
                    result += s[j]
                    j += 2 * numRows - 2 - 2 * i
                    if j < len(s):
                        result += s[j]
                        j += 2 * i

                # print(result)
        return result