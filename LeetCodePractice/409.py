class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        charSet = set()
        for char in s:
            if char in charSet:
                charSet.remove(char)
            else:
                charSet.add(char)
        if len(charSet) == 0:
            return len(s)
        else:
            return len(s) - len(charSet) + 1