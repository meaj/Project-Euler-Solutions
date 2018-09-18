"""
This program finds the sum of the digits in a given factorial
By Kevin Moore
"""

from proj_euler_000 import get_digit_sum, factorial_recur

# We can simply reuse the get_digit_sum and factorial_reur functions
def main():
    print(get_digit_sum(factorial_recur(100)))

main()