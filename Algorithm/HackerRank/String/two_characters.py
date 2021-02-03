#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


# Complete the alternate function below.
def alternate(s):
    if len(s) == 1:
        return 0

    unique = set(s)

    # 가장 긴 alternating 문자열의 길이
    longest = 0

    # 파이썬은 c++의 STL처럼 조합/순열을 지원한다.
    # combinations(counter, 2)의 경우 counter의 key에서 2개의 문자로 이뤄진 조합을 돌려준다.
    # abc -> (a,b), (a,c), (b,c)
    for pair in combinations(unique, 2):
        # 조합 안의 두 글자에 글자에 해당하는 글자만 찾는다.
        matches = [c for c in s if c in pair]

        # zip(matches, matches[1:]) : matches를 두 글자씩 묶은 리스트 튜플을 돌려준다.
        # abae -> (a,b), (b,a), (a,e)
        # 그리고 모든 경우에 각 튜플의 두 글자 c1,c2가 서로 다르다면 alternating한다고 볼 수 있다.
        if all(c1 != c2 for c1, c2 in zip(matches, matches[1:])):
            longest = max(longest, len(matches))

    return longest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()