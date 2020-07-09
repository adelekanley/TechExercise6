import unittest
import calc

class TestCalc(unittest.TestCase):
        def test_add(self):
            result = calc.add(2,4)
            self.assertEqual(result, 6)
            # Or directly 
            self.assertEqual(calc.add(3,3), 6)
            #Edge cases
            self.assertEqual(calc.add(-1,-1), -2)
            self.assertEqual(calc.add(-1,1), 0)

        def test_subtract(self):
            self.assertEqual(calc.subtract(3,3), 0)
            #Edge cases
            self.assertEqual(calc.subtract(0,-1), 1)
            self.assertEqual(calc.subtract(-1,-1), 0)

        def test_multiply(self):
            self.assertEqual(calc.multiply(3,3), 9)
            #Edge cases
            self.assertEqual(calc.multiply(-1,-1), 1)
            self.assertEqual(calc.multiply(-1,1), -1)

        def test_divide(self):
            self.assertEqual(calc.divide(3,3), 1)
            #Edge cases
            self.assertEqual(calc.divide(-1,-1), 1)
            self.assertEqual(calc.divide(-1,1), -1)

            with self.assertRaises(ValueError):
                calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()