'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input 0:
3

Sample Output 0:
3

Sample Input 1:
za

Sample Output 1:
Bad String

'''

########## Failed ###########
# if __name__ == '__main__':
#     S = input().strip()
#     try:
#         print (int(S))
#     except ValueError:
#         print ("Bad String")
#############################


######### Passed ############
S = input().strip()
try:
    print (int(S))
except ValueError:
    print ("Bad String")
#############################
