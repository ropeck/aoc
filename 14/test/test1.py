#!/usr/bin/python3
import unittest
import step1

class TestStep1TestInputLength(unittest.TestCase):
    def runTest(self):
        self.assertEqual([[('498', '4'), ('498', '6'), ('496', '6')],
                          [('503', '4'), ('502', '4'), ('502', '9'), ('494', '9')]],
                         step1.Drawing("test/test_input").d)

#498,4 -> 498,6 -> 496,6
#503,4 -> 502,4 -> 502,9 -> 494,9
