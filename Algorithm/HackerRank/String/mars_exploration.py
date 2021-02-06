#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the marsExploration function below.
def marsExploration(s):
    count, i, j = 0, 0, 0
    tmp = ('S', 'O', 'S')

    for i in range(len(s)):
        if j == 3:
            j = 0
        if s[i] != tmp[j]:
            count += 1
        j += 1
    return (count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()