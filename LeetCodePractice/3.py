class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp = ''
        longest = 0
        for i in range(len(s)):
            if s[i] not in tmp:
                tmp += s[i]
            else:
                if len(tmp) > longest:
                    longest = len(tmp)
                tmp = tmp[tmp.index(s[i])+1:] + s[i]

        if len(tmp) > longest:
            longest = len(tmp)

        return longest
