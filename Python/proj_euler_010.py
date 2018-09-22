"""
This program finds the sum of all primes less than 2,000,000
By Kevin Moore
"""

from proj_euler_000 import is_prime

'''
Sum of Primes function
Returns the sum of all primes less than int_val
'''
def sum_primes(int_val):
    int_sum = 0
    for i in range(1, int_val+1):
        if is_prime(i):
            int_sum += i
    return int_sum

def main():
    int_max = 2000000
    int_sum = sum_primes(int_max)
    print("The sum of all primes less than " + str(int_max) + " is " + str(int_sum))


main()

