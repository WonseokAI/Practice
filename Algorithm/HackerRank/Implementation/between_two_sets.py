#!/bin/python3

import math
import os
import random
import re
import sys
from math import gcd


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# 최소 공배수
def lcm(a, b):
    return int(a * b / gcd(a, b))


def get_lcm(arr):
    cur_lcm = arr[0]
    for i in range(1, len(arr)):
        cur_lcm = lcm(cur_lcm, arr[i])
    return cur_lcm


def get_gcd(arr):
    cur_gcd = arr[0]
    for i in range(1, len(arr)):
        cur_gcd = gcd(cur_gcd, arr[i])
    return cur_gcd


def getTotalX(a, b):
    # Write your code here
    mylist = []
    lcm_a = get_lcm(a)
    gcd_b = get_gcd(b)

    count = 1
    while True:
        element = lcm_a * count
        count += 1
        if element > gcd_b:
            break
        if gcd_b % element != 0:
            continue
        mylist.append(element)

    return len(mylist)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()