'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
12.00
20
8

Sample Output:
15

''''

def solve(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost * tip_percent) / 100
    tax = (meal_cost * tax_percent) / 100
    totalCost = int(round(meal_cost + tip + tax))
    print(totalCost)


if __name__ == '__main__':
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    solve(meal_cost, tip_percent, tax_percent)
