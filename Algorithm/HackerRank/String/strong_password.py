#!/bin/python3

import math
import os
import random
import re
import sys

# https://wikidocs.net/1669


# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    changes = 0
    if not re.search('[0-9]', password):
        changes += 1
    if not re.search('[a-z]', password):
        changes += 1
    if not re.search('[A-Z]', password):
        changes += 1
    if not re.search(r'[!@#$%^&*()\-+]', password):
        changes += 1
    if (changes + n) < 6:
        changes += 6 - (changes + n)

    return changes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
