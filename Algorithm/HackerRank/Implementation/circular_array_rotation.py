#!/bin/python3

import math
import os
import random
import re
import sys


# int a[n]: the array to rotate
# int k: the rotation count
# int queries[1]: the indices to report

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    leng = len(a)

    ans = []
    for q in queries:
        ans.append(a[(leng - k + q) % leng])

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()