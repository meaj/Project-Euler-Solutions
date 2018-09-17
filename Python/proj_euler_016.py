"""
This program finds the sum of the digits of a given power of 2
By Kevin Moore
"""


# Gets the sum of the digits of the value passed into it
def get_digit_sum(int_value):
    int_sum = 0
    str_value = str(int_value)
    for i in str_value:
        int_sum += int(i)
    return int_sum


def main():
    int_exp = int(input("Enter the power of two to get the digit sum of: "))
    print("The sum of the digits of 2^" + str(int_exp) + " is " + str(get_digit_sum(2**int_exp)))

main()