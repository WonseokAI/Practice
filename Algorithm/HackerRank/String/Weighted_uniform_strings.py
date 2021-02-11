#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    weights = set()
    prev = -1
    length = 0
    for c in s:
        weight = ord(c) - ord('a') + 1
        weights.add(weight)
        if prev == c:
            length += 1
            weights.add(length * weight)
        else:
            prev = c
            length = 1

    rval = []
    for q in queries:
        if q in weights:
            rval.append("Yes")
        else:
            rval.append("No")
    return rval


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()