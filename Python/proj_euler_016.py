"""
This program finds the sum of the digits of a given power of 2
By Kevin Moore
"""


from proj_euler_000 import get_digit_sum


def main():
    int_exp = int(input("Enter the power of two to get the digit sum of: "))
    print("The sum of the digits of 2^" + str(int_exp) + " is " + str(get_digit_sum(2**int_exp)))

main()