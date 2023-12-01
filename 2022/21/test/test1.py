#!/usr/bin/python3
import unittest
import step1

class TestStep1_1(unittest.TestCase):
    def runTest(self):
        self.assertEqual(152, step1.main("test/input"))
