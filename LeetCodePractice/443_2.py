class Solution:
    def compress(self, chars: List[str]) -> int:

        # 双指针解法
        l, r = 0, 0
        
        while r < len(chars):
            count = 0
            curr = chars[r]
            while r < len(chars) and chars[r] == curr:
                r += 1
                count += 1

            if count > 1:
                chars[l] = curr
                l += 1
                for c in str(count):
                    chars[l] = c
                    l += 1
            else:
                chars[l] = curr
                l += 1

        return(chars[:l])