#!/usr/bin/python
# -*- coding: utf8 -*-

import unittest
import mspace
import mspace_test
from sets import Set

class EmptyBKTest(mspace_test.EmptyTreeTest):

    def setUp(self):
        self.tree = mspace.BKTree()

class FullBKTest(mspace_test.FullTreeTest):

    def setUp(self):
        self.tree = mspace.BKTree(mspace_test.objects, mspace.levenshtein)
        self.expectedHeight = 4   # TODO
        # BKTrees store exactly one distinct object per node, every pair of
        # objects (x, y) in the index which is equal according to the distance
        # function has be stored in the same node
        self.expectedNumNodes = len(Set(mspace_test.objects))
