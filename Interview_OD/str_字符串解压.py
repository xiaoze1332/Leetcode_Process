class Solution:
    def decodeString(self, s: str) -> str:

        # s = '3[a2[c]]'
        # s = '3[a]2[bc]'
        # s = '2[abc]3[cd]ef'

        
        l, r = 0, 0

        stack = []
        l_stack = []
        r_stack = []

        num = 0
        res_str = ''

        for i, c in enumerate(s):
            if c == '[':
                l_stack.append(i)
                stack.append(s[i-1])
            elif c == ']':
                r_stack.append(i)
                #print(stack.pop())
                num = int(stack.pop())
                tmp_str = s[l_stack.pop()+1:r_stack.pop()]
                res_str += tmp_str * num
            else:
                continue

        return res_str