class Solution:
    def twoSum(self, nums, target):
        for indexi, i in enumerate(nums):
            for indexj, j in enumerate(nums):
                if indexi != indexj and i + j == target:
                    return [indexi, indexj]
        return "target not found"