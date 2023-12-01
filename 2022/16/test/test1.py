#!/usr/bin/python3
import unittest
import step1

class TestStep1(unittest.TestCase):
    def runTest(self):
        part1, part2 = step1.main("test/input")
        self.assertEqual(1651, part1)

class TestStep2(unittest.TestCase):
    def runTest(self):
        part1, part2 = step1.main("test/input")
        self.assertEqual(1707, part2)
