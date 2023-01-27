class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(s) for s in strs])
        for i in range(min_len):
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:min_len]