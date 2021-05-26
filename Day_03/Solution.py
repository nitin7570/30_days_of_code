'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input 0:
3

Sample Output 0:
Weird

Sample Input 1:
24

Sample Output 1:
Not Weird

''''

def check(number):
    if number%2 == 0:
        if number in range(2,6):
            print('Not Weird')
        if number in range(6,21):
            print('Weird')
        if number > 20:
            print('Not Weird')
    else:
        print('Weird')


if __name__ == '__main__':
    N = int(input().strip())
    check(N)
