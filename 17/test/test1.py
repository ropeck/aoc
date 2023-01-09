#!/usr/bin/python3
import unittest
import step1

class TestStep1(unittest.TestCase):
    def runTest(self):
        self.assertEqual(3068, step1.main("test/input", 2022))
