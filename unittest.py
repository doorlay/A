import unittest
from funcs import *

class TestFunctions(unittest.TestCase):

    def test_getPrice(self):
        self.assertGreater(getPrice("AAPL"),10)

if __name__ == '__main__':
    unittest.main()