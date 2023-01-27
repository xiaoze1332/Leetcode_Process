class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        new_list = []
        for i, num in enumerate(nums):
            sum += num
            new_list.append(sum)
        return new_list