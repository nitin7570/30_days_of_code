'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
6
3
5
4
7
2
1

Sample Output:
3 2 5 1 4 7 

'''

###### Below code block was given ######
import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
########################################

    def levelOrder(self,root):
        nodes_to_search = []
        traversed_nodes = ""
        nodes_to_search.append(root)
        while len(nodes_to_search) > 0:
            node = nodes_to_search.pop(0)
            if node.left:
                nodes_to_search.append(node.left)
            if node.right:
                nodes_to_search.append(node.right)
            traversed_nodes += str(node.data) + " "
        print(traversed_nodes)

###### Below code block was given ######
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
########################################
