import collections


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        tmp1 = collections.Counter(nums1)
        tmp2 = collections.Counter(nums2)

        return list((tmp1 & tmp2).elements())