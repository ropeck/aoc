#!/usr/bin/python3
import unittest
import step1

class TestStep1TestInputLength(unittest.TestCase):
    def runTest(self):
        self.assertEqual(13140, step1.main("test_input"))