import unittest
from rabin_karp import rabin_karp

class TestRabin_karp(unittest.TestCase):

    def test_multiple_hits(self):
        string = "AABAACAADAABAABA"
        pattern = "AABA"
        self.assertTrue(rabin_karp(string, pattern), [0,9,12])

    def test_pattern_with_numeric(self):
        string = "ab12a"
        pattern = "b1"
        self.assertEquals(rabin_karp(string, pattern), [1])
    
    def test_no_match(self):
        string = "ab123456"
        pattern = "cd"
        self.assertEquals(rabin_karp(string,pattern),[])



if __name__ == '__main__':
    unittest.main()