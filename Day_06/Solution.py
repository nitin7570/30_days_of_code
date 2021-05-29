'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
2
Hacker
Rank

Sample Output:
Hce akr
Rn ak

'''

class Solution():
    def seperate_string(self, strings):
        final_string_list = []
        for string in strings:
            result_str1 = ''
            result_str2 = ''
            i = 0
            while i < len(string):
                if i % 2==0:
                    result_str1 += string[i]
                else:
                    result_str2 += string[i]
                i += 1
            final_string_list.append(result_str1 +" "+ result_str2)
        print(*final_string_list, sep='\n')

if __name__ == "__main__":
    strings = []
    for _ in range(int(input())):
        strings.append(input().strip())
    solution = Solution()
    solution.seperate_string(strings)