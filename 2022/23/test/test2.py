import unittest

import step2

class TestStep2TestInputLength(unittest.TestCase):
    def runTest(self):
        self.assertEqual(20, step2.main("test/input-big"))

if __name__ == '__main__':
    unittest.main()
