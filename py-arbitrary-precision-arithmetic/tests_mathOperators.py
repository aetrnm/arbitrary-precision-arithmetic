import unittest
from BigNumberCreator import createBigNumber
from Exceptions import InvalidValueError


class MyTestCase(unittest.TestCase):
    positiveNumber1 = createBigNumber('12345')
    positiveNumber2 = createBigNumber('12345')

    negativeNumber1 = createBigNumber('-12345')
    negativeNumber2 = createBigNumber('-12345')

    divisor = 113

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_additionOfPositives(self):
        self.assertEqual(self.positiveNumber1 + self.positiveNumber2, createBigNumber('24690'))

    def test_additionOfNegatives(self):
        self.assertEqual(self.negativeNumber1 + self.negativeNumber2, createBigNumber('-24690'))

    def test_multiplicationOfPositives(self):
        self.assertEqual(self.positiveNumber1 * self.positiveNumber2, createBigNumber('152399025'))

    def test_multiplicationOfNegatives(self):
        self.assertEqual(self.negativeNumber1 * self.negativeNumber2, createBigNumber('152399025'))

    def test_subtractionOfPositives(self):
        self.assertEqual(self.positiveNumber1 - self.positiveNumber2, createBigNumber('0'))

    def test_subtractionOfNegatives(self):
        self.assertEqual(self.negativeNumber1 - self.negativeNumber2, createBigNumber('0'))

    def test_floordiv(self):
        self.assertEqual(self.positiveNumber1 // self.divisor, createBigNumber('109'))

    def test_mod(self):
        self.assertEqual(self.positiveNumber1 % self.divisor, 28)

    def test_invalidInput(self):
        with self.assertRaises(InvalidValueError):
            createBigNumber('hello')

    def test_getFloorIntegerSquareRoot(self):
        # TODO: implement
        pass

    def test_equals(self):
        # TODO: implement
        pass

    def test_notEquals(self):
        # TODO: implement
        pass

    def test_getSign(self):
        # TODO: implement
        pass


if __name__ == '__main__':
    unittest.main()
