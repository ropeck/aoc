#!/usr/bin/python3
import unittest
import step2

class TestStep2(unittest.TestCase):
    def runTest(self):
        self.assertEqual(58, step2.main("True"))
