#!/usr/bin/python3
import unittest
import step2

class TestStep1_1(unittest.TestCase):
    def runTest(self):
        self.assertEqual(1623178306, step2.main("test/input"))

class TestStep1_1mod(unittest.TestCase):
    def runTest(self):
        self.assertEqual(1623178306, step2.main("test/input", True))

class TestStep1mod(unittest.TestCase):
    def runTest(self):
        self.assertEqual(3760092545849, step2.main("input", True))

class TestStep1(unittest.TestCase):
    def runTest(self):
        self.assertEqual(3760092545849, step2.main("input"))

