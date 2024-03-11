from unittest import TestCase

from core import calculate_score
from main import make_list_of_tuples

class test_core_functions(TestCase):
    def test_calculate_score(self):
       self.assertEqual((3, 3), calculate_score(True, True)) 
       self.assertEqual((1, 1), calculate_score(False, False))
       self.assertEqual((5, 1), calculate_score(False, True))
       self.assertEqual((1, 5), calculate_score(True, False))
       
    def test_make_list_of_tuples(self):
        self.assertEqual([], make_list_of_tuples([]))
        self.assertEqual([('a', 'a')], make_list_of_tuples(['a']))
        self.assertEqual([('a', 'a'), ('a', 'b'), ('b', 'b')], make_list_of_tuples(['a', 'b']))
        self.assertEqual([('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')], make_list_of_tuples(['a', 'b', 'c']))
        self.assertEqual([('a', 'a'), ('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'b'), ('b', 'c'), ('b', 'd'), ('c', 'c'), ('c', 'd'), ('d', 'd')], make_list_of_tuples(['a', 'b', 'c', 'd']))