def twoSum(nums: list(), target: int):
    m = {}
    for i in range(len(nums)):
        if nums[i] in m:
            return [i, m[nums[i]]]
        m[target - nums[i]] = i


print(twoSum([5, 5, 2, 8], 10))
print(twoSum([2, 7, 11, 15], 9))