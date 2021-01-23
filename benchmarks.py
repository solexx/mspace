#!/usr/bin/python
# -*- coding: utf8 -*-

import sys, random, time, gc
from codecs import open
import mspace
from mspace import BKTree, VPTree, levenshtein, tokenizer

def get_sample(objects, num):
    objects = list(objects)
    random.shuffle(objects)
    return objects[:num]

def build_tree(cls, objects, metric):
    tree = cls(objects, metric)
    return tree

def benchmark_k(tree, objects, min_dist, max_dist, step):
    mspace.dist_ctr = 0
    print "#%s, size: %s, height: %s, nodes: %s" % (type(tree), len(tree),
            tree.height, tree.num_nodes)
    print "#doing %s searches" % len(objects)
    print "#k\t%6s\t%8s\t%8s\t%8s" % (
            "time", "distCt", "ratio", "resCt")
    for k in range(min_dist, max_dist+1, step):
        print "%s\t" % k,
        start = time.time()
        num_results = 0
        for o in objects:
            num_results += len(tree.search(o, k))
        end = time.time()
        time_per_object = float((end - start)) / len(objects)
        dist_per_object = float(mspace.dist_ctr) / len(objects)
        time_per_dist = time_per_object / dist_per_object
        res_per_object = float(num_results) / len(objects)
        print "%6.4f\t%8.2f\t%0.6f\t%8.2f" % (
                time_per_object, dist_per_object,
                time_per_dist, res_per_object)
        mspace.dist_ctr = 0

def benchmark_construction(cls, objects, metric, max, step):
    print "#%s" % (cls)
    print "#%8s\t%7s\t%12s\t%8s" % ("size", "height", "time", "per node")
    for n in range(step, max+1, step):
        lst = objects[:n]
        start = time.time()
        t = build_tree(cls, lst, metric)
        end = time.time()
        buildtime = float(end) - start
        time_per_node = buildtime / len(t)
        print "%8s\t%7s\t%12.2f\t%8.6f" % (len(t), t.height, buildtime,
                time_per_node)
        del t
        gc.collect()
    print


def main():
    filename = sys.argv[1]
    num = int(sys.argv[2])
    file = open(filename, encoding='iso-8859-1')
    objects = get_sample(tokenizer(file), num)
    file = open(filename, encoding='iso-8859-1')
    toSearch = get_sample(tokenizer(file), min(100, max(int(.01*num), 20)))
    gc.collect()
    for cls in [BKTree, VPTree]:
        print
        #benchmark_construction(cls, objects, levenshtein, num, int(num/6))
        tree = build_tree(cls, objects, levenshtein)
        benchmark_k(tree, toSearch, 0, 3, 1)
        del tree
        garbage = gc.collect()
        #print "#garbage collection threw away %s objects." % garbage

if __name__ == '__main__':
#    sys.stderr.write("""
#WARNING! For several reasons, the following numbers are highly inaccurate.
#For more accurate numbers, use the `timeit` module and disable shuffling of
#objects in tree indexing.\n
#""")
    try:
        main()
    except KeyboardInterrupt, e:
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stderr.write("\n^C\n")


# vim: set et ts=4 sw=4 tw=76 nu:
