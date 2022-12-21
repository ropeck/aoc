#!/usr/bin/python3
import unittest
import step2

class TestStep1_1(unittest.TestCase):
    def runTest(self):
        self.assertEqual(301, step2.main("test/input"))
