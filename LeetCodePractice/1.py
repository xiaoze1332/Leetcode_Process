class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        
        fi = 0
        li = len(nums) - 1

        while fi < li:
            if nums_sorted[fi] + nums_sorted[li] > target:
                li -= 1
            elif nums_sorted[fi] + nums_sorted[li] < target:
                fi += 1
            else:
                a, b = nums_sorted[fi], nums_sorted[li]
                break
        
        if a != b:    
            return [nums.index(a), nums.index(b)]
        else:
            return [nums.index(a), nums.index(b, nums.index(a)+1)]
