'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
STDIN   Function
-----   --------
3       __elements[] size N = 3
1 2 5   __elements = [1, 2, 5]

Sample Output:
4

'''

class Difference:
    def __init__(self, a):
        self.__elements = a

	def computeDifference(self):
        self.maximumDifference = abs(max(self.__elements) - min(self.__elements))


_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()
print(d.maximumDifference)
