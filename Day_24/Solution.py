'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
6
1
2
2
3
3
4

Sample Output:
1 2 3 4 

'''

###### Below code block was given ######
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
#########################################

    def removeDuplicates(self,head):
        if not head:
            return None
        current = head
        while current.next:
            if current.next.data == current.data:
                current.next = current.next.next
            else:
                current = current.next
        return head

###### Below code block was given ######
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 
########################################