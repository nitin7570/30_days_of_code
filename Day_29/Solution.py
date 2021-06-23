'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
STDIN   Function
-----   --------
3       T = 3
5 2     N = 5, K = 2
8 5     N = 8, K = 5
2 2     N = 8, K = 5

Sample Output:
1
4
0

'''

import math
import os
import random
import re
import sys

def bitwiseAnd(N, K):
    max_bitwise = 0
    for i in range(1, N+1):
        for j in range(1, i):
            bitwise = i & j
            if max_bitwise < bitwise < K:
                max_bitwise = bitwise
                if max_bitwise == (K-1):
                    return max_bitwise
    return max_bitwise
    
###### Below code block was given ######   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
##########################################
