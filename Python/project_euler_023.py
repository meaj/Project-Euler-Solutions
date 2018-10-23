"""
This program finds the sum of all numbers that cannot be written as the sum of two abundant numbers
By Kevin Moore
"""

# Maximum possible value not written as a sum of two abundant numbers
LIMIT = 28123


# return the sum or the proper divisors of the provided value
def sum_proper_divisors( int_val ):
    int_sum = 0
    for i in range (1, int_val):
        if (int_val % i == 0):
            int_sum += 1
    return int_sum

def generate_abundant_numbers():
    lst_abundant = []
    for int_val in range(1, LIMIT):
        int_sum = sum_proper_divisors(int_val)
        if ( int_sum > int_val ):
            lst_abundant.append(int_val)
    return lst_abundant

# generate list of non-abundant sums
def generate_non_abundant_sums( lst_abundant ):
    lst_abundant_sums = []
    lst_non_abundant_sums = []
    # create list of abundant sums first
    # get first value
    for i in range(1, len(lst_abundant)):
        int_a = lst_abundant[i]
        # get remaining values following first value
        for j in range(i, len(lst_abundant)):
            int_b = lst_abundant[j]
            if ( int_a != int_b ) & ( (int_a + int_b) not in lst_abundant_sums ):
                lst_abundant_sums.append(int_a + int_b)
    # sort the list
    lst_abundant_sums.sort()
    # create list of non-abundant sums
    for i in range(1, LIMIT):
        if ( i not in lst_abundant_sums ):
            lst_non_abundant_sums.append(i)
    return lst_non_abundant_sums

# driver	
def main():
    lst_abundant = generate_abundant_numbers()
    lst_abundant_sums = generate_non_abundant_sums(lst_abundant)
    int_out = sum(lst_abundant_sums)
    print(int_out)

main()