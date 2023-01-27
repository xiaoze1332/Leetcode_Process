from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = Counter(s)
        for c in s:
            if c not in stack:
                while stack and stack[-1] > c and counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            counter[c] -= 1
        return ''.join(stack)