import unittest
from BigNumberCreator import createBigNumber
from Exceptions import InvalidValueError


class MyTestCase(unittest.TestCase):
    positiveNumber = createBigNumber('12345')
    negativeNumber = createBigNumber('-12345')

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_additionOfPositives(self):
        self.assertEqual(createBigNumber('12345') + createBigNumber('12345'), createBigNumber('24690'))

    def test_additionOfNegatives(self):
        self.assertEqual(createBigNumber('-12345') + createBigNumber('-12345'), createBigNumber('-24690'))

    def test_multiplicationOfPositives(self):
        self.assertEqual(createBigNumber('12345') * createBigNumber('12345'), createBigNumber('152399025'))

    def test_multiplicationOfNegatives(self):
        self.assertEqual(createBigNumber('-12345') * createBigNumber('-12345'), createBigNumber('152399025'))

    def test_subtractionOfPositives(self):
        self.assertEqual(createBigNumber('12345') - createBigNumber('12345'), createBigNumber('0'))

    def test_subtractionOfNegatives(self):
        self.assertEqual(createBigNumber('-12345') - createBigNumber('-12345'), createBigNumber('0'))

    def test_floordiv(self):
        self.assertEqual(createBigNumber('12345') // 113, createBigNumber('109'))

    def test_mod(self):
        self.assertEqual(createBigNumber('12345') % 113, 28)

    def test_invalidInput(self):
        with self.assertRaises(InvalidValueError):
            createBigNumber('hello')

    def test_getCeilIntegerSquareRoot(self):
        self.assertEqual(createBigNumber('12345').getCeilIntegerSquareRoot(), createBigNumber('112'))

    def test_equals(self):
        self.assertEqual(createBigNumber('12345') == createBigNumber('12345'), True)

    def test_notEquals(self):
        self.assertEqual(createBigNumber('12345') != createBigNumber('-12345'), True)

    def test_getSignPositive(self):
        self.assertEqual(self.positiveNumber.getSign(), 1)

    def test_getSignZero(self):
        self.assertEqual(createBigNumber('0').getSign(), 0)

    def test_getSignNegative(self):
        self.assertEqual(self.negativeNumber.getSign(), -1)


if __name__ == '__main__':
    unittest.main()
