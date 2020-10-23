import unittest

from main import CalculateCircleArea

class TestCircle(unittest.TestCase):
    def test_float(self):
        result = CalculateCircleArea.calculateCircle()
        self.asserEqual(result, 3.8013271108436504)


if __name__ == '__main__':
    unittest.main()
