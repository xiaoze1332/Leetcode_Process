class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def final(input_str):
            stack = []

            for i in input_str:
                if i == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return stack

        return final(s) == final(t)