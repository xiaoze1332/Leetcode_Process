class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if not nums or target < nums[0] or target > nums[-1]:
            return -1

        len_num = int(len(nums))
        res = 0

        while len_num > 1:
            if nums[len_num//2] > target:
                nums = nums[:len_num//2]
            else:
                nums = nums[len_num//2:]
                res += len_num//2
            len_num = int(len(nums))

        if nums[0] == target:
            return res
        else:
            return -1