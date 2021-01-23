#!/usr/bin/python
# -*- coding: utf8 -*-

import unittest
import mspace
import mspace_test
from sets import Set

class EmptyVPTest(mspace_test.EmptyTreeTest):

    def setUp(self):
        self.tree = mspace.VPTree()

    def tearDown(self):
        del(self.tree)


class FullVPTest(mspace_test.FullTreeTest):

    def setUp(self):
        self.tree = mspace.VPTree(mspace_test.objects, mspace.levenshtein)
        self.expectedHeight = 3   # TODO
        # BKTrees store exactly one distinct object per node, every pair of
        # objects (x, y) in the index which is equal according to the distance
        # function has be stored in the same node
        self.expectedNumNodes = len(Set(mspace_test.objects))
