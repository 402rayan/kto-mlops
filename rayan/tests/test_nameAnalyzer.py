import unittest
from rayan.src.nameAnalyzer import NameAnalyzer

"""
Count names with more than seven letters
"""
class TestNameAnalyzer(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        analyzer = NameAnalyzer(prenoms)
        count = analyzer.count_names_too_long()
        self.assertEqual(count, 4)

if __name__ == '__main__':
    unittest.main()