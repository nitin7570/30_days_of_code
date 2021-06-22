'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com

Sample Output:
julia
julia
riya
samantha
tanya

'''

import re


if __name__ == '__main__':
    N = int(input().strip())
    
    pattern = r"@gmail\.com$"
    regex = re.compile(pattern)
    
    firstNameList = []

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        
        if regex.search(emailID):
            firstNameList.append(firstName)
    firstNameList.sort()
    
    for name in firstNameList:
        print(name)
