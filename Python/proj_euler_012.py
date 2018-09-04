"""
This program finds the first triangle number to have over five hundred divisors
By Kevin Moore
"""

import math, time

'''
Get number of divisors function
Returns the number of divisors of a given value n
Takes the integer n as a parameter 
'''
def get_num_divisors(int_val):

    int_count = 0
    # Maximum possible factor is the square root of int_val
    int_end = math.sqrt(int_val)
    # Count from the divisors starting with 1 and ending with the maximum possible factor
    for i in range(1, int(int_end)):
        if (int_val % i == 0):
            int_count += 2
    # Remove int_val^2 from the count
    if (int_val ** 2 == int_val):
        int_count -= 1
    return int_count

'''
Generate triangle number function
Returns the nth triangle number
Takes the integer n as a parameter
'''
def generate_triangle_number(int_target, tval_start):
    int_count = 1
    print("Calculating triangle number with " + str(int_target) + " divisors", end='', flush=True)
    while True:
        int_sum = int_count * (int_count+1) // 2
        if(int_sum % 1000 == 0):
            print(".",end='',flush=True)
        if (get_num_divisors(int_sum) > int_target):
            tval_end = time.monotonic()
            tval_elapsed = tval_end - tval_start
            print('\nDone! Execution time: %s seconds' % tval_elapsed)
            break
        int_count += 1
    return int_sum

def main():
    tval_start = time.monotonic()
    int_target = 500
    int_solution = generate_triangle_number(int_target, tval_start)
    print("The first Triangle number with over " + str(int_target) + " divisors is " + str(int_solution))

main()
