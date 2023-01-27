class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return(-1)
        elif len(nums) == 1:
            if target == nums[0]:
                return(0)
            else:
                return(-1)
        elif len(nums) < 100:
            return nums.index(target) if target in nums else -1
        else:
            l, r = 0, len(nums) - 1

            while(l <= r and target != nums[l] and target != nums[r]):
                if target > nums[l]:
                    l += 1
                elif target < nums[r]:
                    r -= 1
                else:
                    return(-1)
        
        if target == nums[l]:
            return(l)
        elif target == nums[r]:
            return(r)