'''
This program finds the difference in the sum of the squares and the square of the sum of the first 100 natural numbers
By Kevin Moore
'''

'''
Returns the difference in the sum of the squares and the square of the sum of the natural numbers from 1 to int_max
'''
def calculate_diff(int_stop):
    # Calculates the square of the sum of first int_stop natural numbers
    sqr_of_sum = ((int_stop * (int_stop + 1)) // 2) ** 2
    # Adds the square of each of the first int_stop natural numbers
    sum_of_sqr = sum(val**2 for val in range (int_stop + 1))

    return sqr_of_sum - sum_of_sqr

def main():
    print("The difference between the sum of the squares and the square of the sum of the natural number from "
          "1 to 100 is "+ str(calculate_diff(100)))

main()
