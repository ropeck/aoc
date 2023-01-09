#!/usr/bin/python3
import unittest
import step2

class Test2Step1(unittest.TestCase):
    def runTest(self):
        self.assertEqual(1514285714288, step2.main("test/input"))
