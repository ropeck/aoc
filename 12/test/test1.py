#!/usr/bin/python3
import unittest
import step1

class TestStep1TestInputLength(unittest.TestCase):
    def runTest(self):
        self.assertEqual(31, step1.read_drawing("test/test_input"))
