#!/bin/python3

import math
import os
import random
import re
import sys
import math


# Complete the viralAdvertising function below.
def viralAdvertising(n):
    num_adv = 5

    total = 0
    for day in range(n):
        num_liked = num_adv // 2
        total += num_liked
        num_adv = num_liked * 3

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()