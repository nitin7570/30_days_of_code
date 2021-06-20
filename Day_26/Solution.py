'''
Author: Nitin Singh
Email : nitin7570@gmail.com

Sample Input:
STDIN       Function
-----       --------
9 6 2015    day = 9, month = 6, year = 2015 (date returned)
6 6 2015    day = 6, month = 6, year = 2015 (date due)

Sample Output:
45

'''

def calculate_fine(ret_date_str, due_date_str):
    ret_day, ret_mon, ret_year = [int(e) for e in ret_date_str.split(' ')]
    due_day, due_mon, due_year = [int(e) for e in due_date_str.split(' ')]
    if ret_year < due_year:
        print(0)
    elif ret_year == due_year:
        if ret_mon < due_mon:
            print(0)
        elif ret_mon == due_mon:
            if ret_day <= due_day:
                print(0)
            else:
                print( 15 * (ret_day - due_day))
        else:
            print( 500 * (ret_mon - due_mon))
    else:
        print(10000)


if __name__ == "__main__":
    ret_date_str = input()
    due_date_str = input()
    calculate_fine(ret_date_str, due_date_str)
    