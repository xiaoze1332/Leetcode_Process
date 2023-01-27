class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end, longest = 0, 0, 0

        res_list = [[0] * n for i in range(n)]
        res_list

        for i in range(n):
            for j in range(i):
                if s[i] == s[j] and (i - j < 3 or res_list[j + 1][i - 1]):
                    res_list[j][i] = 1
                    if i - j > longest:
                        longest = i - j
                        start, end = j, i

        return s[start:end + 1]
