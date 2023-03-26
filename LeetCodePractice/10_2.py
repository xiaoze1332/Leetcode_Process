class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Dynamic programming
        # dp[i][j] = True if s[:i] matches p[:j]
        # dp[i][j] = dp[i-1][j-1] if p[j-1] != '*'
        # dp[i][j] = dp[i][j-2] if p[j-1] == '*' and the pattern repeats 0 time
        # dp[i][j] = dp[i-1][j] if p[j-1] == '*' and the pattern repeats >= 1 time
        # dp[0][0] = True
        # dp[i][0] = False for i > 0
        # dp[0][j] = dp[0][j-2] if p[j-1] == '*' and the pattern repeats 0 time
        # dp[0][j] = False if p[j-1] == '*' and the pattern repeats >= 1 time
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] and (p[j - 1] in {s[i - 1], '.'})
                else:
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (p[j - 2] in {s[i - 1], '.'}))
        return dp[-1][-1]