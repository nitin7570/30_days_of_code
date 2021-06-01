'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
3

Sample Output:
6

'''

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
if __name__ == '__main__':
    n = int(input())
    print(factorial(n))
    