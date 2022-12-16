#!/usr/bin/python3
import unittest
import step1

class TestStep1(unittest.TestCase):
    def runTest(self):
        self.assertEqual(26, step1.main("test/input", 10))
