# coding=utf-8


class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += 1
            n = n & (n - 1)
        return count
