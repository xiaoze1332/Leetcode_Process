class Solution:
    def decodeString(self, s: str) -> str:

        # s = '3[a2[c]]'
        # s = '3[a]2[bc]'
        # s = '2[abc]3[cd]ef'

        
        stack = []
        left_index_stack = []
        right_index_stack = []

        left_index = 0
        right_index = 0

        num = 0
        CurStr = ''

        for i in range(len(s)):
            if s[i] == '[':
                left_index_stack.append(i)
                stack.append(s[i-1])
            elif s[i] == ']':
                right_index_stack.append(i)
                num = stack.pop()
                left_index = left_index_stack.pop()
                right_index = right_index_stack.pop()

                TmpStr = s[left_index+1:right_index]
                CurStr = s[:left_index-1] + TmpStr*int(num) + s[right_index+1:]


        return CurStr