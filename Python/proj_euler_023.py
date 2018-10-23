"""
This program finds the sum of all numbers that cannot be written as the sum of two abundant numbers
By Kevin Moore
"""

# Maximum possible value not written as a sum of two abundant numbers
LIMIT = 28123
# LIMIT = 25
from proj_euler_000 import gen_set_proper_divisors

def print_status(int_pos, int_max, str_type='Calculation'):
    flt_complete = int_pos / int_max
    print(str_type + " is {:2.5%} complete\r".format(flt_complete), end='')


# Generates a set of abundant numbers less than int_max
def gen_set_abundant_nums(int_max):
    set_abundant = set()

    # Determine if the numbers between 0 and max are abundant (exclusive)
    for i in range(1, int_max):
        print_status(i, int_max)
        if is_abundant(i):
            set_abundant.add(i)

    # Return a sorted set for readability
    return sorted(set_abundant)


# Returns the sum of the set of divisors from gen_set_proper_divisors()
def get_sum_divisors(int_val):
    return sum(gen_set_proper_divisors(int_val))


# Returns true if the provided value is abundant
def is_abundant(int_val):
    if (get_sum_divisors(int_val) > int_val):
        # print(str(int_val) + " is an abundant number")
        return True
    return False


# Returns true if the provided value is the sum of two abundant numbers
def is_abundant_sum(int_val, set_abundant):
    for i in set_abundant:
        # we have passed the possible location of int_val
        if i > int_val:
            return False
        # int_val is an abundant sum
        if (int_val - i) in set_abundant:
            return True
    # int_val was not found in the set of abundant sums
    return False


# Generates a set of non abundant sums less than int_max
def gen_set_non_abundant_sums(int_max):
    print("Generating set of abundant numbers")
    # abundant set
    set_abundant = gen_set_abundant_nums(int_max)
    print("Done with abundant set generation!\n")
    print("Generating set of non-abundant numbers")
    # non-abundant set
    set_non_abundant = set()

    # Determine if the numbers between 0 and max are abundant sums (exclusive)
    for i in range(1, int_max):
        print_status(i, int_max, "Generation")
        if not is_abundant_sum(i, set_abundant):
            set_non_abundant.add(i)

    print("Done with non-abundant set generation!")
    return sorted(set_non_abundant)


# driver for program
def main():
    int_out = sum(gen_set_non_abundant_sums(LIMIT))
    print("The sum of all non-abundant sums less than " + str(LIMIT) + " is " + str(int_out))


main()