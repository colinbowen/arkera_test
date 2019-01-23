import unittest
import copy
import random


def increment_dictionary_values(d, i):
    x = copy.deepcopy(d)
    for k, v in x.items():
        x[k] = v + i
    return x


class TestIncrementDictionaryValues (unittest.TestCase):
    def test_increment_dictionary_values(self):
        d = {'a': 1}
        dd = increment_dictionary_values(d, 1)
        ddd = increment_dictionary_values(d, -1)
        self.assertEqual(dd['a'], 2)
        self.assertEqual(ddd['a'], 0)


unittest.main()