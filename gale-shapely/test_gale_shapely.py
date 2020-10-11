import unittest
from gale_shapely import gale_shapely

class TestGale_Shapely(unittest.TestCase):

    def test_one_to_one(self):
        men = {'a':['A']}
        women = {'A':['a']}
        result = [['a','A']]
        self.assertEqual(gale_shapely(men, women), result)

    def test_three_to_three(self):
        men = {'a':['A','B','C'], 'b':['B','C','A'], 'c':['C','A','B']}
        women = {'A':['b','c','a'],'B':['c','b','a'],'C':['a','b','c']}
        result = [['a','A'],['b','B'],['c','C']]
        self.assertEqual(gale_shapely(men,women), result)

    def test_empty(self):
        self.assertEqual(gale_shapely([],[]),[] )

if __name__ == '__main__':
    unittest.main()