'''
Sample tests
'''

from django.test import SimpleTestCase

from app import calculator

class calculatorTests(SimpleTestCase):
    '''test the module '''

    def test_add_number(self):
        '''test adding number together'''
        res = calculator.add(3, 7,)

        self.assertEqual(res, 10)
    
    def test_subtract_number(self):
        '''test adding number together'''

        res = calculator.subtract(8, 2)

        self.assertEqual(res, 6)


