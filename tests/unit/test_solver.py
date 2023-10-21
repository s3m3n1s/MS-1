import unittest
from solver import calculate


class SolverTestBorder(unittest.TestCase):

    def test_all_null(self):
        self.assertEqual(True, calculate(0, 0, 0))

    def test_lineal(self):
        self.assertEqual([-1.0], calculate(0, 2, 2))

    def test_a(self):
        self.assertEqual([-0.0], calculate(2, 0, 0))

    def test_big_num_no_solut(self):
        self.assertEqual([], calculate(2000000, 1000000, 22222222))

    def test_big_num_solut(self):
        self.assertAlmostEqual([-3.092695, 3.592695][0], calculate(-2000000, 1000000, 22222222)[0], places=6)
        self.assertAlmostEqual([-3.092695, 3.592695][1], calculate(-2000000, 1000000, 22222222)[1], places=6)


class SolverTestSamples(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual([1, -5 / 2], calculate(2, 3, -5), places=6)

    def test_2(self):
        self.assertAlmostEqual([1, 0.4], calculate(5, -7, 2), places=6)

    def test_3(self):
        self.assertAlmostEqual([], calculate(0, 0, 1), places=6)

    def test4(self):
        self.assertAlmostEqual([-1], calculate(0, 1, 1), places=6)

    def test5(self):
        self.assertAlmostEqual([], calculate(1, 1, 1), places=6)


if __name__ == "__main__":
    unittest.main()
