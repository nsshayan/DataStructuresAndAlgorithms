#!/Users/snaganan/anaconda3/bin/python

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    nBinary = bin(n)
    print(nBinary)
    count = 0
    maxCount = 0
    for i in range(2, len(nBinary)):
        if nBinary[i] == '1':
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 0
    if count > maxCount:
        maxCount = count
    print(maxCount)
