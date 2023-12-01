#!/usr/bin/python3
import unittest
import step2

class TestStep2(unittest.TestCase):
    def runTest(self):
        self.assertEqual(56000011, step2.main("test/input", 20))
