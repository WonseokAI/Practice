#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    dic_a = Counter(a)
    max_length = 0
    for i in dic_a.keys():
        if (i + 1) in dic_a.keys():
            max_length = max(dic_a[i] + dic_a[i + 1], max_length)
        else:
            max_length = max(dic_a[i], max_length)

    return max_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()