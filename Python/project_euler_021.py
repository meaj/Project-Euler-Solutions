"""
This program finds the sum of all amicable numbers under 10,000
By Kevin Moore
"""

import math


# Generates a set of the proper divisors of a number int_val
def gen_set_proper_divisors(int_val):
    set_divisors = set()

    # Given 'x % i = 0', there is some value k such that 'i * k = x'.
    # We only need to search up to sqrt(int_val) because all other divisors will be given by i and k
    int_max = int(math.sqrt(int_val))
    # Handles case where int_val is square
    if (int_max ** 2 == int_val):
        set_divisors.add(int_max)
    else:
        int_max += 1

    # Find all divisors between 1 and int_max
    for i in range(1, int_max + 1):
        if int_val % i == 0:  # 'x % i = 0'
            set_divisors.add(i)  # i in 'i * k = x'
            set_divisors.add(int(int_val / i))  # k in 'i * k = x'

    # Ensure int_val is not in set_divisors
    if int_val in set_divisors:
        set_divisors.remove(int_val)

    # Return a sorted set for readability
    return sorted(set_divisors)


# Returns the sum of the set of divisors from gen_set_proper_divisors()
def get_sum_divisors(int_val):
    return sum(gen_set_proper_divisors(int_val))


# Retruns the sum of the amicable numbers under the value int_limit
def get_sum_amicable_numbers(int_limit):
    int_sum = 0

    # Amicable numbers are defined such that 'sum(divisors(x)) = y' and 'sum(divisors(y)) = x' while 'x != y'
    for int_a in range(1, int_limit):
        int_b = get_sum_divisors(int_a)
        if int_a == get_sum_divisors(int_b) and int_a < int_b:
            int_sum += (int_a + int_b)

    return int_sum


def main():
    int_limit = 10000
    print("Calculating the sum of all amicable numbers under " + str(int_limit))
    set_out = get_sum_amicable_numbers(int_limit)
    print("The sum of all the amicable numbers under " + str(int_limit) + " is " + str(set_out))


main()