"""
This program finds the sum of all amicable numbers under 10,000
By Kevin Moore
"""

from proj_euler_000 import gen_set_proper_divisors


# Returns the sum of the set of divisors from gen_set_proper_divisors()
def get_sum_divisors(int_val):
    return sum(gen_set_proper_divisors(int_val))


# Returns the sum of the amicable numbers under the value int_limit
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