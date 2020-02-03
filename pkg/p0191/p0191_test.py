# coding=utf-8

import unittest
from .p0191 import Solution


class TestP0191(unittest.TestCase):

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

    def test_p0191(self):
        self.assertEqual(
            3,
            self.solution.hammingWeight(11)
        )
