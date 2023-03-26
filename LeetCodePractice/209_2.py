class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 双指针法
        l, r = 0, 0
        sums = 0
        minLen = len(nums) + 1
        while r < len(nums):
            sums += nums[r]
            r += 1
            while sums >= target:
                minLen = min(minLen, r - l)
                sums -= nums[l]
                l += 1
        if minLen == len(nums) + 1:
            return 0
        else:
            return minLen