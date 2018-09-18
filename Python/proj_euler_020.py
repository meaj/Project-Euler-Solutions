"""
This program finds the sum of the digits in a given factorial
By Kevin Moore
"""


# Finds the factorial of a value n recursively
def factorial_recur(n):
    if (n == 0):
        return 1
    else:
        return n * factorial_recur(n-1)


# Gets the sum of the digits of the value passed into it
def get_digit_sum(int_value):
    int_sum = 0
    str_value = str(int_value)
    for i in str_value:
        int_sum += int(i)
    return int_sum


def main():
    print(get_digit_sum(factorial_recur(100)))

main()