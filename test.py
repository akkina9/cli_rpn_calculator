import unittest
from rpn import evaluate, operations

class TestSum(unittest.TestCase):
    def test_add(self):
        self.assertEqual(evaluate('5 8 +', True), 13, 'Expected: 13')

    def test_sub(self):
        self.assertEqual(evaluate('5 8 -', True), -3, 'Expected: -3')

    def test_multi(self):
        self.assertEqual(evaluate('5 8 *', True), 40, 'Expected: 40')

    def test_div(self):
        self.assertEqual(evaluate('5 8 /', True), 0.625, 'Expected: 0.625')

    def test_expression_1(self):
        self.assertEqual(evaluate('5 5 5 8 + + - 13 +', True), 0.0, 'Expected: 0.0')

    def test_expression_2(self):
        self.assertEqual(evaluate('-3 -2 * 5 +', True), 11.0, 'Expected: 11.6')

    def test_expression_3(self):
        self.assertEqual(evaluate('5 9 1 - /', True), 0.625, 'Expected: 0.625')


    def test_errorcase_divbyzero(self):
        self.assertEqual(evaluate('5 0 / ', True), 'ZeroDivisionError', 'Expected: - ZeroDivisionError')        

    def test_errorcase_1(self):
        self.assertEqual(evaluate('5 - ', True), 'Stack too small to apply operation. So ignoring the last operator.', 'Expected: - Stack too small to apply operation. So ignoring the last operator.')

    def test_errorcase_2(self):
        self.assertEqual(evaluate('5 5 ^ ', True), 'Please type in valid number or supported operator (' + str(list(operations.keys())) + ')' , 'Expected: - Please type in valid number or supported operator...')        

if __name__ == '__main__':
    unittest.main()