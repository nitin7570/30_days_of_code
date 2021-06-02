'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input 1:
5

Sample Output 1:
1

Sample Input 2:
13

Sample Output 2:
2

'''

def find_consecutive_num(n):
    binary = []
    while n > 0:
        remainder = n % 2 
        binary.append(remainder)
        n = n//2
    number_string = "".join(str(digit) for digit in binary)
    return (max(map(len, number_string.split('0'))))
    
if __name__ == '__main__':
    print(find_consecutive_num(13))
    