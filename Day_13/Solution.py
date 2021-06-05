'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
The following input from stdin is handled by the locked stub code in your editor:
The Alchemist
Paulo Coelho
248

Sample Output:
The following output is printed by your display() method:
Title: The Alchemist
Author: Paulo Coelho
Price: 248

'''

### This code snippet is given already ###
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
##########################################


class MyBook(Book):
    
    price = 0
    
    def __init__(self, title, author, price):
        super(Book, self).__init__()
        self.price = price 

    def display(self):
        print("Title: " +title)
        print("Author: " +author)
        print("Price: " +str(price))


### This code snippet is given already ###
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
##########################################