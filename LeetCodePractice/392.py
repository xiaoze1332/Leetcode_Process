class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        for i, x in enumerate(s):
            if x not in t:
                return False
            else:
                t = t[t.index(x)+1:]

        return True