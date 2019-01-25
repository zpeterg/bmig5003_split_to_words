import unittest
from index import dealArgs, getAndFilter

options = {'start': 'foo', 'stop': 'bar', 'finish': 'enough'}
words = [
    'fish',
    'hat',
    'foo',
    'cow',
    'siamese',
    'wonderland',
    'foo',
    'toothpaste',
    'bar',
    'umbrella',
    'foo',
    'milky',
    'flight-manual',
    'toothpick',
    'bar',
    'enough',
    'event-horizon',
    'bar'
]


args = [
    '-file=small_test.txt',
    '-start=foo',
    '-stop=bar',
    '-finish=enough',
]


class GetAndFilterTest(unittest.TestCase):
    def test_args_print(self):
        res = {
            'file': 'small_test.txt',
            'start': 'foo',
            'stop': 'bar',
            'finish': 'enough',
        }
        self.assertEqual(res, dealArgs(args))

    def test_get_and_filter_simple(self):
        res = [
            'cow',
            'siamese',
            'wonderland',
            'toothpaste',
            'milky',
            'flight-manual',
            'toothpick',
        ]
        self.assertEqual(getAndFilter(args), res)


if __name__ == '__main__':
    unittest.main()

