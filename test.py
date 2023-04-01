import unittest
from memo import Memoizator, CopyMemoizator, CustomMemoizator

def factorial(n):
    if ( n==0 ):
        return 1
    else:
        return n*factorial(n-1)

class MemoizationTests(unittest.TestCase):
    def test_basic_memoization(self):
        memoized_factorial = Memoizator(factorial)
        memoized_factorial(5)
        self.assertEqual(memoized_factorial.cache[(5,)], 120)
        self.assertEqual(memoized_factorial(5), 120)

    def test_copy_memoization(self):
        memoized_factorial = CopyMemoizator(factorial)
        memoized_factorial(5)
        self.assertEqual(memoized_factorial.cache[(5,)], 120)
        self.assertEqual(memoized_factorial(5), 120)

    def test_custom_memoization(self):
        memoized_factorial = CustomMemoizator(factorial, lambda x: 2*x)
        memoized_factorial(5)
        self.assertEqual(memoized_factorial.cache[(5,)], 120)
        self.assertEqual(memoized_factorial(5), 240)


class MemoizationDecoratorTests(unittest.TestCase):
    def test_basic_memoization(self):
        @Memoizator
        def memoized_factorial(n):
            if ( n==0 ):
                return 1
            else:
                return n*factorial(n-1)

        memoized_factorial(5)
        self.assertEqual(memoized_factorial.cache[(5,)], 120)
        self.assertEqual(memoized_factorial(5), 120)



if __name__ == '__main__':
    unittest.main()

