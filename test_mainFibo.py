from mainFibo import fibonacci_3 as fb
import unittest


class testFibonacci(unittest.TestCase):

    def test_Fibonacci1_is_1(self):
        primer_valor = 1
        segundo_valor = fb(1)
        self.assertEqual(primer_valor, segundo_valor, "error")

    def test_Fibonacci9_is_34(self):
        self.assertEqual(34, fb(9), "ERROR")

    def test_fibonacci_negative_raise_exception(self):
        with self.assertRaises(ValueError):
            fb(-10)


if __name__ == '__main__':
    unittest.main()
