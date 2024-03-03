from unittest import TestCase

from core import calculate_score

class test_core_functions(TestCase):
    def test_calculate_score(self):
       self.assertEqual((3, 3), calculate_score(True, True)) 
       self.assertEqual((1, 1), calculate_score(False, False))
       self.assertEqual((5, 1), calculate_score(False, True))
       self.assertEqual((1, 5), calculate_score(True, False))
       
       