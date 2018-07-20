# Project Euler Problem 3
# 		A solution to problem 3 from projecteuler.net
#		By Kevin Moore

import math

# Returns the largest prime factor of val
def prime_factor(val):
    # The largest possible prime factor, will be less than the square root of the value
    max_fac = int(math.sqrt(val))

    # Factors out 2 until result is odd or 2 is reached
    while (val % 2 == 0):
        if (val == 2):
            break
        val = val / 2
    # Factors out i until result is greater than max_fac or greatest factor is reached
    for i in range(3, max_fac, 2):
        if ( val  == i):
            break
        while (val % i == 0):
            val = val // i
    return val

def main():
    orig = 600851475143
    val = prime_factor(orig)
    print("The largest prime factor of " + str(orig) + " is " + str(val))

main()
