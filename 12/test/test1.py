#!/usr/bin/python3
import unittest
import step1
import step2

class TestStep1(unittest.TestCase):
    def runTest(self):
        self.assertEqual(31, step1.main("test/test_input"))

class TestStep2(unittest.TestCase):
    def runTest(self):
        self.assertEqual(29, step2.main("test/test_input"))
