#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    bird_dic = {}

    for i in arr:
        if i not in bird_dic:
            bird_dic[i] = 1
        else:
            bird_dic[i] += 1

    bird_dic_list = bird_dic.values()

    max_num = max(bird_dic_list)

    max_list = []

    for j in bird_dic.keys():
        if bird_dic.get(j) == max_num:
            max_list.append(j)

    return min(max_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
