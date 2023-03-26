from functools import reduce

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        # 判断是否有重复的字符
        tmp_set = []
        # 用于存储所有的子串
        res_set = []
        l, r = 0, 1

        tmp_set.append(s[l])

        while l < len(s) and r < len(s):
            if s[r] not in tmp_set:
                tmp_set.append(s[r])
                r += 1
            else:
                res_set.append(tmp_set)
                tmp_set = []
                l += 1
                r = l + 1
                tmp_set.append(s[l])

        res_set.append(tmp_set)

        print(res_set)

        return reduce(lambda x, y: x if x > y else y, map(lambda x: len(x), res_set))   # 返回最长的子串长度

