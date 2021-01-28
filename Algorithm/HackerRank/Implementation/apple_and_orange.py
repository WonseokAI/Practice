#!/bin/python3

import math
import os
import random
import re
import sys


# s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    num_apples = 0
    num_oranges = 0

    for i in range(len(apples)):
        if s <= apples[i] + a and apples[i] + a <= t:
            num_apples += 1

    print(num_apples)

    for i in range(len(oranges)):
        if s <= oranges[i] + b and oranges[i] + b <= t:
            num_oranges += 1

    print(num_oranges)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)