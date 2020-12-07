import unittest
from inf24 import main


class MyTestCase(unittest.TestCase):
    def test_a(self):
        self.assertEqual(main('()'), 1)

    def test_b(self):
        self.assertEqual(main('('), 0)

    def test_c(self):
        self.assertEqual(main(')'), 0)

    def test_d(self):
        self.assertEqual(main(')('), 0)

    def test_e(self):
        self.assertEqual(main('())()()'), 2)

    def test_f(self):
        self.assertEqual(main(')()(()()(()()())'), 3)

    def test_g(self):
        self.assertEqual(main('((()))'), 1)


if __name__ == '__main__':
    unittest.main()

