#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for x in range(1,len(arr)):
        key =arr[x]
        i=x-1
        while(key<=arr[i] and i>=0):
            arr[i+1]=arr[i]
            i=i-1
        arr[i+1]=key
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
