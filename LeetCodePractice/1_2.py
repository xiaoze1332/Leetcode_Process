class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            
            if (target - x) in nums:
                if nums.index(target - x) != i:
                    return [i, nums.index(target - x)]