from math import factorial


def calc_number(n, k):
    number = factorial(n) / (factorial(k) * factorial(n-k))

    return number


def pascal_triangle(n):
    row_list = ""

    for row in range(n):
        for k in range(row+1):
            number = calc_number(row, k)
            row_list += str(int(number)) + " "
        print(row_list)
        row_list = ""


n = int(input())

pascal_triangle(n)
