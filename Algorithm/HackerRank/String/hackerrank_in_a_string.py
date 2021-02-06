#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    original = deque(['h','a','c','k','e','r','r','a','n','k'])
    for ch in s:
        if not original:
            return "YES"
        if ch == original[0]:
            original.popleft()
    if original:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()