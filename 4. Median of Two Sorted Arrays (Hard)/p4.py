class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        length = len(nums)
        i = length // 2
        if length % 2:
            return nums[i]
        else:
            return (nums[i-1] + nums[i]) / 2
