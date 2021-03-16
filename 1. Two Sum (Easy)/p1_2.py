class Solution(object):
    def twoSum(self, nums, target):
        subtract = {}
        for i in range(len(nums)):
            if nums[i] in subtract:
                return [i, subtract[nums[i]]]
            subtract[target - nums[i]] = i
