from collections import deque

class Solution:
    def isPalindrome(self, x: int) -> bool:
        d = deque(str(x))

        while len(d) > 1:
            if d.popleft() != d.pop():
                return False

        return True