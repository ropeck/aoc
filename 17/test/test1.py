#!/usr/bin/python3
import unittest
import step1

class TestStep1(unittest.TestCase):
    def runTest(self):
        tower = step1.main("test/input", 2022)
        self.assertEqual(3068, tower.height())
