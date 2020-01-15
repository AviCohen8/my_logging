import unittest
from homeworks import dvir as d


class MyTestCase(unittest.TestCase):

    def test_something(self):
        result = d.filter_and_divide(344, 544, 444)
        self.assertEqual(result, 'zipped data: [(344, 34.4), (544, 54.4), (444, 44.4)]', 'hi')

    def test_something1(self):
        result = d.log_scale([100, 200])
        self.assertEqual(result, 'zipped data: [(100, 4.605170185988092), (200, 5.298317366548036)]', 'hi2')

    def test_something2(self):
        result = d.uneven([100, 200])
        self.assertEqual(result, 'zipped data: [(100, 100)]', 'HI3')


if __name__ == '__main__':
    unittest.main()
