class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        set_nums = set(nums)
        dict_nums = {}

        for num in nums:
            if num in dict_nums:
                dict_nums[num] += 1
            else:
                dict_nums[num] = 1

        for key, value in dict_nums.items():
            if value == 1:
                continue
            else:
                set_nums.remove(key)

        return set_nums.pop()