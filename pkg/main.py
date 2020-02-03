# coding=utf-8

import unittest
import os
import importlib


def _loadTestcasesFromDir(dirpath, lastDir):
    cases = []
    for filename in os.listdir(dirpath):
        filepath = os.path.join(dirpath, filename)
        if os.path.isfile(filepath) and filename.endswith('_test.py'):
            testModule = importlib.import_module('{}.{}'.format(
                lastDir, filename[:-3]))
            for attrname in dir(testModule):
                attrvalue = getattr(testModule, attrname)
                if (isinstance(attrvalue, type) and
                        issubclass(attrvalue, unittest.TestCase)):
                    cases.append(
                        unittest.TestLoader().loadTestsFromTestCase(attrvalue))
    return cases


def loadTestcases(dirpath):
    cases = []
    for filename in os.listdir(dirpath):
        filepath = os.path.join(dirpath, filename)
        if os.path.isdir(filepath) and filename.startswith('p'):
            cases = cases + _loadTestcasesFromDir(filepath, filename)

    return cases


if __name__ == '__main__':
    suites = unittest.TestSuite(loadTestcases(os.getcwd()))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suites)
