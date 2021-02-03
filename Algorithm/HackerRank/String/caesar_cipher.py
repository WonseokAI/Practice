#!/bin/python3

import math
import os
import random
import re
import sys

# string s: cleartext
# int k: the alphabet rotation factor

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    result = ""
    for i in range(len(s)):
        if not s[i].isalpha():
            result += s[i]
            continue
        if s[i].isupper():
            result += chr((ord(s[i]) + k - 65) % 26 + 65)
        else:
            result += chr((ord(s[i]) + k - 97) % 26 + 97)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
