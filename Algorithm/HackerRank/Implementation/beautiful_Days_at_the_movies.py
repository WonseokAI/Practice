#!/bin/python3

import math
import os
import random
import re
import sys


# int i: the starting day number
# int j: the ending day number
# int k: the divisor

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    rev = 0
    count = 0
    for day in range(i, j + 1):
        if day % 10 == 0:
            rev = int(str(day // 10)[::-1])
        else:
            rev = int((str(day)[::-1]))
        if abs(day - rev) % k == 0:
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()