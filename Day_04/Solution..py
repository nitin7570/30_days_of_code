'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
4
-1
10
16
18

Sample Output:
Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.

''''

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.age = 0
        if initialAge > 0:
            self.age = initialAge
        else:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif self.age in range(13, 18):
            print("You are a teenager.")
        else:
            print("You are old.")
        
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1

# The code below this line is given already by HackerRank
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")