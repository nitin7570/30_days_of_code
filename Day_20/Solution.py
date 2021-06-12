'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input 0:
3
1 2 3

Sample Output 0:
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3

Sample Input 1:
3
3 2 1

Sample Output 1:
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3

'''

def bubble(arr):
    count_swap = 0
    for num in range(len(arr)-1, 0, -1):
        for i in range(num):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count_swap +=1
    return count_swap

    
if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    print("Array is sorted in {} swaps.".format(bubble(a)))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
