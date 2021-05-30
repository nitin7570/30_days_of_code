'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
4
1 4 3 2

Sample Output:
2 3 4 1

'''

class Solution():

    # Approach 1
    def reverse_appr_1(arr):
        for element in list(reversed(arr)):
            print(element,end=" ")

    # Approach 2
    def reverse_appr_2(arr):
        i = len(arr)-1
        while i>=0:
            print(arr[i], end=" ")
            i -= 1

    # Approach 3
    def reverse_appr_3(arr):
        print((" ".join(str(element) for element in arr))[::-1])
    
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    solution = Solution()
    solution.reverse_appr_3(arr)