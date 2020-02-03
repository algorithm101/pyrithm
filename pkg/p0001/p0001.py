# coding=utf-8


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mark = {}
        for index, num in enumerate(nums):
            solve = target - num
            if solve in mark:
                return [mark[solve], index]
            mark[num] = index
        return []
