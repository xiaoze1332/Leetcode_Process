class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 判断sums中是否含有target
        def isContain(target, sums):
            if target in sums:
                return True
            else:
                return False

        # 二分查找
        def binarySearch(target, sums):
            left = 0
            right = len(sums) - 1
            while left <= right:
                mid = (left + right) // 2
                if sums[mid] == target:
                    return mid
                elif sums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        # 求和
        sums = [0]

        for i in range(len(nums)):
            sums.append(sums[i] + nums[i])

        # 求最小长度
        minLen = len(nums) + 1
        for i in range(len(sums)):
            if isContain(target + sums[i], sums):
                minLen = min(minLen, binarySearch(target + sums[i], sums) - i)
        if minLen == len(nums) + 1:
            return 0
        else:
            return minLen