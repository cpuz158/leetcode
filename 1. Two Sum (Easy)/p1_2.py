class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        subtract = {}
        for i in range(len(nums)):
            if nums[i] in subtract:
                return [i, subtract[nums[i]]]
            subtract[target - nums[i]] = i
