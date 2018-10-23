"""
This file serves to store commonly used functions in the Python solutions
By Kevin Moore
"""

from math import sqrt


# Checks if a value val is prime or not. Returns true or false respectively
def is_prime(val):
    # handles case where the number to be tested is less than 2
    if val < 2:
        return False

    # checks primality of the number from 2 to sqrt(val)
    for number in range(2, int(sqrt(val) + 1)):
        if val % number == 0:
            return False

    return True


# Finds the factorial of a value n recursively
def factorial_recur(n):
    if (n == 0):
        return 1
    else:
        return n * factorial_recur(n-1)


# Finds the binomial coefficient of two values n and k
def n_choose_k(n, k):
    return factorial_recur(n) / (factorial_recur(k) * factorial_recur(n - k))


# Gets the sum of the digits of the value passed into it
def get_digit_sum(int_value):
    int_sum = 0
    str_value = str(int_value)
    for i in str_value:
        int_sum += int(i)
    return int_sum


# Finds the longest path through a triangle
def find_triangle_path(lst_input):
    # Copy the input into an empty triangle that can store the maximum path of each sub triangle at given indices
    lst_paths = lst_input
    # Starting at the second from the bottom row, add up the maximum value of the lower neighbors of a given index
    for row in reversed(range(len(lst_input) - 1)):
        for col in range(len(lst_input[row])):
            lst_paths[row][col] += max(lst_input[row+1][col], lst_input[row+1][col+1])
        # FROM TESTING PLEASE IGNORE:
        # print("The max paths of rows " + str(row) + " and " + str(row+1))
        # print(lst_paths[row])
    # After calculation, the maximum value will be at the top
    return lst_paths[0][0]


# Generates a set of the proper divisors of a number int_val
def gen_set_proper_divisors(int_val):
    set_divisors = set()

    # Given 'x % i = 0', there is some value k such that 'i * k = x'.
    # We only need to search up to sqrt(int_val) because all other divisors will be given by i and k
    int_max = int(sqrt(int_val))
    # Handles case where int_val is square
    if (int_max ** 2 == int_val):
        set_divisors.add(int_max)
    else:
        int_max += 1

    # Find all divisors between 1 and int_max (inclusive)
    for i in range(1, int_max + 1):
        if int_val % i == 0:  # 'x % i = 0'
            set_divisors.add(i)  # i in 'i * k = x'
            set_divisors.add(int(int_val / i))  # k in 'i * k = x'

    # Ensure int_val is not in set_divisors
    if int_val in set_divisors:
        set_divisors.remove(int_val)
    # print(str(int_val) + ':' + str(sorted(set_divisors)))
    # Return a sorted set for readability
    return sorted(set_divisors)