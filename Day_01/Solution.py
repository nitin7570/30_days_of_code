'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
12
4.0
is the best place to learn and practice coding!

Sample Output:
16
8.0
HackerRank is the best place to learn and practice coding!

''''

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
second_integer = 0
second_double = 0.0
second_string = ''

# Read and save an integer, double, and String to your variables.
second_integer = int(input())
second_double = float(input())
second_string = str(input())

# Print the sum of both integer variables on a new line.
print(i + second_integer)

# Print the sum of the double variables on a new line.
print(d + second_double)

# Concatenate and print the String variables on a new line
print(s + second_string)
# The 's' variable above should be printed first.
