class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hashmap = {}

        for i, x in enumerate(s):
            if x not in hashmap:
                hashmap[x] = t[i]
            else:
                if hashmap[x] != t[i]:
                    return False

        return len(hashmap) == len(set(hashmap.values()))
