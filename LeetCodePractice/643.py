class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums) / k
        else:
            tmp_list = []
            i = 0
            while(i < (len(nums) - k)):
                tmp_list.append(sum(nums[i:i+k]))
                i += 1
            
            return max(tmp_list) / k

# 测试
if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    s = Solution()
    # 结果正确则打印True
    print(s.findMaxAverage(nums, k) == 12.75)