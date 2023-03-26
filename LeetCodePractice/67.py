class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 判断a和b的长度，将较短的字符串补0，使得两个字符串长度相等
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        else:
            a = '0' * (len(b) - len(a)) + a

        # 从后往前遍历字符串，将两个字符串对应位置的字符相加，如果有进位，则将进位标志位置1
        carry = 0
        res = ''
        for i in range(len(a) - 1, -1, -1):
            tmp = int(a[i]) + int(b[i]) + carry
            if tmp >= 2:
                carry = 1
                tmp -= 2
            else:
                carry = 0
            res = str(tmp) + res

        # 如果最后还有进位，则将进位标志位置1
        if carry == 1:
            res = '1' + res

        return res