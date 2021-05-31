'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Sample Output:
sam=99912222
Not found
harry=12299933

'''

n = int(input())
names_numbers = [input().split() for _ in range(n)]
phonebook = {name : number for name, number in names_numbers}
while True:
    try:
        name = input()
        if name in phonebook:
            print("{}={}".format(name, phonebook[name]))
        else:
            print('Not found')
    except:
        break