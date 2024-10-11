import unittest
from simple_calculator import SimpleCalculator


class SimpleCalculator (unittest.TestCase):
    #Set up the SimpleCalculator instance before each test
    def setUp(self):
        self.calc=SimpleCalculator()

    def test_addition(self):

        #Test the addition method.
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(4, 2.3), 6.3)

    def test_subtract(self):

        # test the subtract method
        self.assertEqual(self.calc.subtract(5,7), -2)
        self.assertEqual(self.calc.subtract(8,1), 7)
        self.assertEqual(self.calc.subtract(1.6,0.6), 1)
        

    def test_multiply(self):

        # test the multiply method
        self.assertEqual(self.calc.multiply(2,2), 4)
        self.assertEqual(self.calc.multiply(9,0), 0)

    def test_divide(self):

        # test the divide method
        self.assertEqual(self.calc.divide(6,2), 3)
        self.assertEqual(self.calc.divide(0,4), 0)
        self.assertEqual(self.calc.divide(10,0), None)


if __name__ == "__main__":
  unittest.main()



        

        





