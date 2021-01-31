#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxi = scores[0]
    mini = scores[0]
    return_list = [0, 0]

    for score in scores:
        if score > maxi:
            return_list[0] += 1
            maxi = score
        elif score < mini:
            return_list[1] += 1
            mini = score

    return (str(return_list[0]), str(return_list[1]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()