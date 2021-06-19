'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
3
12
5
7

Sample Output:
Not prime
Prime
Prime

'''

import math

def isPrime(n):
    if n <= 1:
        return False
    sqrt_n = math.sqrt(n)
    if sqrt_n.is_integer():
        return False
    for i in range(2, int(sqrt_n)+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        if isPrime(n):
            print("Prime")
        else:
            print("Not prime")
