'''
This program finds the sum of all primes less than 2,000,000
By Kevin Moore
'''

from math import sqrt

'''
Primality Check Function
Checks if a value int_val is prime or not. Returns true or false respectively
'''
def is_prime(int_val):
    # handles case where the number to be tested is less than 2
    if int_val < 2:
        return False

    # checks primality of the number from 2 to sqrt(int_val)
    for number in range(2, int(sqrt(int_val) + 1)):
        if int_val % number == 0:
            return False

    return True

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

