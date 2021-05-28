'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
2

Sample Output:
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

''''

result = lambda a:a*i

if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1,11):
        
        # Using lambda
        print("{0} x {1} = {2}".format(n, i, result(i)))
        
        # Usual approach
        # print("{0} x {1} = {2}".format(n, i, n*i))
