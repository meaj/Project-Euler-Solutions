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