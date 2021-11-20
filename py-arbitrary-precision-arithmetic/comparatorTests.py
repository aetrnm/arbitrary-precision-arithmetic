from BigNumberCreator import createBigNumber
import unittest


class GreaterThanTests(unittest.TestCase):

    def test_Positive_GT_Negative(self):
        self.assertEqual(createBigNumber('10') > createBigNumber('-10'), True, "Should be True")

    def test_Negative_GT_Positive(self):
        self.assertEqual(createBigNumber('-10') > createBigNumber('10'), False, "Should be False")

    def test_Positive_GT_Self(self):
        self.assertEqual(createBigNumber('10') > createBigNumber('10'), False, "Should be False")

    def test_Negative_GT_Self(self):
        self.assertEqual(createBigNumber('-10') > createBigNumber('-10'), False, "Should be False")

    def test_ten_GT_one(self):
        self.assertEqual(createBigNumber('10') > createBigNumber('1'), True, "Should be True")

    def test_ten_GT_twenty(self):
        self.assertEqual(createBigNumber('10') > createBigNumber('20'), False, "Should be False")

    def test_Zero_GT_One(self):
        self.assertEqual(createBigNumber('0') > createBigNumber('1'), False, "Should be False")

    def test_Zero_GT_Zero(self):
        self.assertEqual(createBigNumber('0') > createBigNumber('0'), False, "Should be False")

    def test_Zero_GT_NegativeOne(self):
        self.assertEqual(createBigNumber('0') > createBigNumber('-1'), True, "Should be True")

    def test_NegativeTen_GT_NegativeTwenty(self):
        self.assertEqual(createBigNumber('-10') > createBigNumber('-20'), True, "Should be True")

    def test_NegativeTen_GT_NegativeOne(self):
        self.assertEqual(createBigNumber('-10') > createBigNumber('-1'), False, "Should be False")


if __name__ == '__main__':
    unittest.main()
