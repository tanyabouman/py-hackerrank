#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/maximum-subarray-sum/problem
# some weird modulo trick
# https://stackoverflow.com/questions/31113993/maximum-subarray-sum-modulo-m
#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#

# binary tree package is missing insert, update, delete functions
# https://pypi.org/project/binary-tree/
# this package has more of those functions, but still not a find minimum
# greater than
# https://pypi.org/project/self-balancing-binary-search-tree/
# ugh, hackerrank doesn't allow sbbst, or even binary_tree
# implement the solution without trees
# https://stackoverflow.com/a/65961749

def maximumSum(a, m):
    # sums[0]: index in the initial array
    # sums[1]: mod sum of all the elements so far
    sums = [(0, a[0] % m)]
    for i in range(1, len(a)):
        sums.append((i, (sums[i-1][1] + a[i]) % m))
    sums.sort(key=(lambda x: x[1]))

    # search through the array for the minimum gap that is in order of the
    # input
    # maximum value starts with the maximum mod in the sum array
    result = sums[-1][1]

    for i in range(1, len(sums)):
        if sums[i-1][0] > sums[i][0] and sums[i-1][1] < sums[i][1]:
            result = max(result, (m-sums[i][1]+sums[i-1][1]) % m)

    return result
