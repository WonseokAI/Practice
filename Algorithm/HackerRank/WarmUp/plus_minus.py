#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    plus = 0
    minus = 0
    zero = 0
    leng = len(arr)

    for i in arr:
        if i > 0:
            plus += 1
        elif i < 0:
            minus += 1
        else:
            zero += 1

    print('{:,.6f}'.format(plus / leng))
    print('{:,.6f}'.format(minus / leng))
    print('{:,.6f}'.format(zero / leng))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)