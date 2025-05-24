import unittest
from main import multiply

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(1, 2), 2)

if __name__ == '__main__':
    unittest.main()

