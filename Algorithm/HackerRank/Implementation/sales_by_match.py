#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sucks = {}
    count = 0
    for sock in ar:
        if sock not in sucks:
            sucks[sock] = 1
            continue
        if sucks[sock] == 1:
            count += 1
            sucks[sock] = 0
        elif sucks[sock] == 0:
            sucks[sock] = 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()