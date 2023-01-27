class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        set_nums = set(nums)

        if target not in set_nums:
            return [-1, -1]
        else:
            return [nums.index(target), len(nums) - nums[::-1].index(target) - 1]