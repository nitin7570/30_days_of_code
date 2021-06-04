'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
Heraldo Memelli 8135627
2
100 80

Sample Output:
Name: Memelli, Heraldo
ID: 8135627
Grade: O

'''

class Person:

	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
    
    def calculate(self):
        sum_of_score = sum(scores)
        num_of_score = len(scores)
        a_s = sum_of_score/num_of_score
        if a_s < 40:
            return "T"
        elif a_s < 55:
            return "D"
        elif a_s < 70:
            return "P"
        elif a_s < 80:
            return "A"
        elif a_s < 90:
            return "E"
        else:
            return "O"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())