import imp


import unittest
import calc


class testCalc(unittest.TestCase):
    def test_sum(self):
        result = calc.sum(3, 7)
        self.assertEqual(10, result)

    ## self.assertEqual(9, result) //fail TC(예외)
    def test_minus(self):
        self.assertEqual(5, calc.minus(10, 5))
