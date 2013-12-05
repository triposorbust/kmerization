import kmerize as km
import unittest

class KmerizeSpec(unittest.TestCase):
    """Describe: Function kmerize converts a string to its k-mers."""
    def test_short(self):
        """It should return an empty dictionary for len(s) < k."""
        self.assertEquals({}, km.kmerize("ABCDEFG", 10))
    def test_kmers(self):
        """It should correctly count kmers!"""
        test_string = "AABCCABCCABC"
        expected = [("AAB", 1),
                    ("ABC", 3),
                    ("BCC", 2),
                    ("CCA", 2),
                    ("CAB", 2)]
        computed = km.kmerize(test_string, 3)
        for kmer,expect in expected:
            self.assertEquals(expect, computed[kmer])

class KmergeSpec(unittest.TestCase):
    """Describe: Function kmerge takes two dictionaries and sums on key."""
    def test_empty(self):
        """It should returns identical dictionaries merging with empty."""
        adict = { "A": 1, "B": 2, "C": 3 }
        self.assertEquals(adict, km.kmerge(adict, {}))
        self.assertEquals(adict, km.kmerge({}, adict))
    def test_sum(self):
        """It should sum redundant keys."""
        adict = { "A": 1, "B": 2, "C": 3 }
        bdict = { "B": 4, "C": 5, "D": 9 }
        expected = [("A",1), ("B",6), ("C",8), ("D", 9)]
        computed = km.kmerge(adict, bdict)
        for key,expect in expected:
            self.assertEquals(expect, computed[key])

if __name__ == "__main__":
    unittest.main()
