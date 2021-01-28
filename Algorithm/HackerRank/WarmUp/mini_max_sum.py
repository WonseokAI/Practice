#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum_arr = sum(arr)
    mini = sum_arr - max(arr)
    maxi = sum_arr - min(arr)

    print(mini, maxi)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)