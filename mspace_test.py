#!/usr/bin/python
# -*- coding: utf8 -*-

import unittest
import mspace

class LevenshteinTest(unittest.TestCase):

    def testEmptyStrings(self):
        assert mspace.levenshtein("", "") == 0

    def testEqualStrings(self):
        assert mspace.levenshtein("abc", "abc") == 0

    def testInsertion(self):
        assert mspace.levenshtein("", "a") == 1

    def testDeletion(self):
        assert mspace.levenshtein("a", "") == 1

    def testReplacement(self):
        assert mspace.levenshtein("a", "b") == 1

    def testSwap(self):
        assert mspace.levenshtein("ab", "ba") == 2

    def testAll(self):
        assert mspace.levenshtein("bbbcccd", "abbbcce") == 3

class EmptyTreeTest(unittest.TestCase):

    def testHeight(self):
        assert self.tree.height == 1

    def testSize(self):
        assert len(self.tree) == 0

    def testNumNodes(self):
        assert self.tree.num_nodes == 1

    def testSearch(self):
        assert self.tree.search(None, 0) == []

    def testIsEmpty(self):
        assert not self.tree

    def testChildren(self):
        assert len(self.tree.children) == 0

    def testIsRoot(self):
        assert self.tree.is_root()

    def testIsLeaf(self):
        assert self.tree.is_leaf()


class FullTreeTest(unittest.TestCase):

    def testSize(self):
        assert len(self.tree) == len(objects)

    def testNumNodes(self):
        assert self.tree.num_nodes == self.expectedNumNodes

    def testHeight(self):
        #print self.tree.height
        assert self.tree.height == self.expectedHeight

    def testSearch(self):
        for k in (0, 1, 2, 3):
            result = self.tree.search(obj, k)
            assert len(results[k]) == len(result)
            for o in result:
                assert o in results[k]

# test objects to insert into metric space
objects = [ "aaa aaa", "aaa aaa",  # (distance = 0) equal
            "aba aaa", "aaa aba",  # distance = 1 to first
            "abb aaa", "aaa abb",  # distance = 2
            "bbb aaa", "aaa bbb" ] # distance = 3

# test object to search for
obj = objects[0]

# mapping from distance to obj to expected result list
results = { 0: objects[:2],
            1: objects[:4],
            2: objects[:6],
            3: objects[:8] }


if __name__ == '__main__':
    from bktree_test import EmptyBKTest, FullBKTest
    from vptree_test import EmptyVPTest, FullVPTest
    tests = (
            unittest.TestLoader().loadTestsFromTestCase(LevenshteinTest),
            unittest.TestLoader().loadTestsFromTestCase(EmptyBKTest),
            unittest.TestLoader().loadTestsFromTestCase(EmptyVPTest),
            unittest.TestLoader().loadTestsFromTestCase(FullBKTest),
            unittest.TestLoader().loadTestsFromTestCase(FullVPTest)
    )
    alltests = unittest.TestSuite(tests)
    unittest.TextTestRunner(verbosity=2).run(alltests)
