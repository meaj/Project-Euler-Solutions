'''
This program finds the 10,001st prime number
By Kevin Moore
'''

from proj_euler_000 import is_prime

'''
Nth Prime Generation Function
This function will generate the nth prime by counting the number of primes generated until int_val is reached
'''
def generate_prime_n(int_val):
    prime_count = 0
    test_val = 1
    # test numbers for primality until the int_val prime is encountered
    while (prime_count < int_val):
        # if a prime number is encountered, increase the prime count
        if is_prime(test_val):
            prime_count += 1
        test_val += 1
    return test_val - 1

def main():
    val = 10001
    print("The #" + str(val) + " prime is " + str(generate_prime_n(val)))

main()