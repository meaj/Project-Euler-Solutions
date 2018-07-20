'''
This program will find the least common multiple of a range of values from 1 to 20
By Kevin Moore
'''

'''
Binary Greatest Common Divisor function
Calculates the greatest common divisor of two non negative integers, int_a and int_b
Returns the gcd as expressed by gcd(a,b) = g *(2^d), where int_a corresponds to a and int_b corresponds to b
'''
def binary_gcd(int_a, int_b):
    # exp will correspond to d
    exp = 0
    # divide out 2 while both values are even and increment exp
    while int_a % 2 == 0 and int_b % 2 == 0:
        int_a /= 2
        int_b /= 2
        exp += 1
    # reduce int_a and int_b until they are equal, which will correspond to g
    while int_a != int_b:
        # if int_a is still even, divide by 2 and continue
        if int_a % 2 == 0:
            int_a /= 2
        # if int_b is still even, divide by 2 and continue
        elif int_b % 2 == 0:
            int_b /= 2
        # if int_a is larger than int_b, make int_a even by setting it to half the difference of int_a and int_b
        elif int_a > int_b:
            int_a = (int_a - int_b)/2
        # if int_b is larger than int_a, make int_b even by setting it to half the difference of int_b and int_a
        else:
            int_b = (int_b - int_a)/2
    # returns the gcd as gcd(a,b) = g*(2^d)
    return int_a * (2 ** exp)


'''
Iterative Least Common Multiple of a Range function
calculates the lcm for a range of values where lcm(a,b) = a * b / gcd(a,b)
this iterates through each value in the range, updating max (corresponds to a) by
setting it to the lcm of the current maximum and the current val (corresponds to b) at each step in the range
since max = 1 to start, the range can begin at 2
'''
def iterative_lcm(int_a, int_b):
    max = int_a

    for val in range(int_a, int_b+1):
        max = max * val // binary_gcd(val, max)

    return max


def main():
    print(str(iterative_lcm(1,20)))


main()
