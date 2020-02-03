# coding=utf-8

import unittest
from .p0001 import Solution


class TestP0001(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    def test_p0001(self):
        self.assertEqual([0, 1], self.solution.twoSum([2, 7, 11, 15], 9))
