class Solution:
    def isPalindrome(self, x: int) -> bool:

        str_x = str(x)

        length = len(str_x)


        # only compare the first half and the last half, speed up the process
        if length % 2 == 0:
            return str_x[:length//2] == str_x[length//2:][::-1]
        else:
            return str_x[:length//2] == str_x[length//2+1:][::-1]